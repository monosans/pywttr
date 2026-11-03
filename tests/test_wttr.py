from __future__ import annotations

import httpx2
import pytest
from pydantic import AnyHttpUrl

import pywttr


@pytest.mark.parametrize(
    "language", [lang for lang in pywttr.Language if lang is not pywttr.Language.EN]
)
def test_wttr_without_session(language: pywttr.Language) -> None:
    with pywttr.Wttr() as wttr:
        weather = wttr.weather("Paris", language=language)
    assert isinstance(weather, language._model_)


def test_wttr_with_session() -> None:
    language = pywttr.Language.EN

    with httpx2.Client(timeout=httpx2.Timeout(60, connect=5), follow_redirects=True) as session:
        wttr = pywttr.Wttr(session=session)
        weather = wttr.weather("Paris", language=language)
    assert isinstance(weather, language._model_)


def test_wttr_base_url_default() -> None:
    assert pywttr.Wttr().base_url == AnyHttpUrl("https://wttr.in")


def test_wttr_base_url_custom() -> None:
    base_url = AnyHttpUrl("https://example.com/wttr")
    assert pywttr.Wttr(base_url=base_url).base_url == base_url


def test_wttr_close_without_session() -> None:
    wttr = pywttr.Wttr()
    assert wttr.session is None
    wttr.close()
    assert wttr.session is None


def test_wttr_close_closes_passed_session() -> None:
    session = httpx2.Client()
    with pywttr.Wttr(session=session) as wttr:
        assert wttr.session is session
    assert session.is_closed
