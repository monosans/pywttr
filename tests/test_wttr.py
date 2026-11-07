from __future__ import annotations

import inspect
import subprocess
import sys

import httpx2
import pytest
from pydantic import AnyHttpUrl, ValidationError

import pywttr


@pytest.mark.parametrize(
    "language", [lang for lang in pywttr.Language if lang is not pywttr.Language.EN]
)
def test_wttr_without_session(language: pywttr.Language) -> None:
    with pywttr.Wttr() as wttr:
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


def test_weather_keeps_its_signature() -> None:
    signature = inspect.signature(pywttr.Wttr.weather)
    assert list(signature.parameters) == ["self", "location", "language"]
    assert signature.parameters["language"].default is pywttr.Language.EN
    assert signature.return_annotation == "pywttr_models.AnyModel"


@pytest.mark.parametrize(
    ("location", "language"), [(1, pywttr.Language.DE), ("Paris", "not-a-language")]
)
def test_weather_validates_its_arguments(location: object, language: object) -> None:
    wttr = pywttr.Wttr()
    with pytest.raises(ValidationError, match=r"validation error for Wttr\.weather"):
        wttr.weather(location, language=language)  # type: ignore[call-overload]
    # The session is created just before the request, so none was sent.
    assert wttr.session is None


def test_import_leaves_the_return_type_of_weather_unevaluated() -> None:
    """Evaluating `pywttr_models.AnyModel` would import every language's models."""
    code = (
        "import pywttr_models\n"
        "vars(pywttr_models).pop('AnyModel', None)\n"
        "def __getattr__(name):\n"
        "    raise AttributeError(name)\n"
        "pywttr_models.__getattr__ = __getattr__\n"
        "import pywttr\n"
    )
    subprocess.run((sys.executable, "-c", code), check=True)  # noqa: S603
