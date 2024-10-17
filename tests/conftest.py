from __future__ import annotations

from collections.abc import Iterator

import pydantic.v1 as pydantic
import pytest
from requests import Session


@pytest.fixture(scope="session")
def http_session() -> Iterator[Session]:
    with Session() as s:
        yield s


@pytest.fixture
def location() -> str:
    return "Paris"


@pytest.fixture(autouse=True)
def _pydantic_strict(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(pydantic.BaseConfig, "extra", pydantic.Extra.forbid)
    monkeypatch.setattr(pydantic.BaseConfig, "validate_all", True)
    monkeypatch.setattr(pydantic.BaseConfig, "validate_assignment", True)
