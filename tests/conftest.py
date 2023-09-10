from __future__ import annotations

from typing import Iterator

import pytest
from pydantic.v1 import BaseConfig, Extra
from requests import Session


@pytest.fixture(scope="session")
def http_session() -> Iterator[Session]:
    with Session() as s:
        yield s


@pytest.fixture()
def location() -> str:
    return "Paris"


@pytest.fixture(autouse=True)
def _pydantic_strict(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(BaseConfig, "extra", Extra.forbid)
    monkeypatch.setattr(BaseConfig, "validate_all", True)
    monkeypatch.setattr(BaseConfig, "validate_assignment", True)
