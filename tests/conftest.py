from __future__ import annotations

import pytest

try:
    from pydantic.v1 import BaseConfig, Extra
except ImportError:
    from pydantic import BaseConfig, Extra  # type: ignore[assignment]


@pytest.fixture(autouse=True)
def _pydantic_strict(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(BaseConfig, "extra", Extra.forbid)
    monkeypatch.setattr(BaseConfig, "validate_all", True)
    monkeypatch.setattr(BaseConfig, "validate_assignment", True)
