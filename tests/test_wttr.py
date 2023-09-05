from __future__ import annotations

import pytest
from requests import Session

import pywttr

pytestmark = pytest.mark.filterwarnings(
    "ignore::aiopywttr.WttrClassDeprecationWarning"
)


@pytest.mark.parametrize("language", pywttr.Language)
def test_wttr(
    location: str, language: pywttr.Language, http_session: Session
) -> None:
    wttr = pywttr.Wttr(location, session=http_session)
    model = getattr(wttr, language._name_.lower())()
    assert isinstance(model, language._model_)


def test_wttr_without_session(location: str) -> None:
    wttr = pywttr.Wttr(location)
    language = pywttr.Language.EN
    model = getattr(wttr, language._name_.lower())()
    assert isinstance(model, language._model_)
