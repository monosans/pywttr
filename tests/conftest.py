from __future__ import annotations

from collections.abc import Iterator

import pydantic
import pytest

import pywttr


def _get_models(
    cls: type[pydantic.BaseModel] = pydantic.BaseModel, /
) -> Iterator[type[pydantic.BaseModel]]:
    for subclass in cls.__subclasses__():
        if subclass.__module__.startswith(f"{pywttr.models.__name__}."):
            yield subclass
        yield from _get_models(subclass)


@pytest.fixture(autouse=True)
def _pydantic_forbid_extra(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    models = tuple(_get_models())
    with monkeypatch.context() as m:
        for model in models:
            m.setitem(model.model_config, "extra", "forbid")
            model.model_rebuild(force=True)
        yield
    for model in models:
        model.model_rebuild(force=True)
