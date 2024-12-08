from __future__ import annotations

import pytest
from requests import Session

import pywttr


@pytest.mark.parametrize(
    "language",
    [lang for lang in pywttr.Language if lang is not pywttr.Language.EN],
)
def test_wttr_without_session(language: pywttr.Language) -> None:
    with pywttr.Wttr() as wttr:
        weather = wttr.weather("Paris", language=language)
    assert isinstance(weather, language._model_)


def test_wttr_with_session() -> None:
    language = pywttr.Language.EN

    with Session() as s:
        wttr = pywttr.Wttr(session=s)
        weather = wttr.weather("Paris", language=language)
    assert isinstance(weather, language._model_)
