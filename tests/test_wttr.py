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


def test_wttr_english_descriptions() -> None:
    """wttr.in sends no `lang_en` or `lang_xx` for English, so both give `weather_desc`."""
    with pywttr.Wttr() as wttr:
        weather = wttr.weather("Paris", language=pywttr.Language.EN)
    assert weather.current_condition
    for current in weather.current_condition:
        assert current.lang_en == current.lang_xx == current.weather_desc
    hours = [hour for day in weather.weather for hour in day.hourly]
    assert hours
    for hour in hours:
        assert hour.lang_en == hour.lang_xx == hour.weather_desc


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


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("", "/Paris?format=j1&lang=de"),
        ("/wttr", "/wttr/Paris?format=j1&lang=de"),
        ("/wttr/", "/wttr/Paris?format=j1&lang=de"),
    ],
)
def test_wttr_request_url(path: str, expected: str) -> None:
    requests: list[httpx2.Request] = []

    def handler(request: httpx2.Request) -> httpx2.Response:
        requests.append(request)
        return httpx2.Response(
            200, json={"current_condition": [], "nearest_area": [], "request": [], "weather": []}
        )

    with httpx2.Client(transport=httpx2.MockTransport(handler)) as session:
        wttr = pywttr.Wttr(base_url=AnyHttpUrl(f"https://wttr.in{path}"), session=session)
        wttr.weather("Paris", language=pywttr.Language.DE)
    assert [str(request.url) for request in requests] == [f"https://wttr.in{expected}"]
