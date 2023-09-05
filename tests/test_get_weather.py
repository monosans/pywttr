from __future__ import annotations

import pytest
from requests import Session

import pywttr


@pytest.mark.parametrize("language", pywttr.Language)
def test_get_weather(
    location: str, language: pywttr.Language, http_session: Session
) -> None:
    model = pywttr.get_weather(location, language, session=http_session)
    assert isinstance(model, language._model_)


def test_get_weather_without_session(location: str) -> None:
    language = pywttr.Language.EN
    model = pywttr.get_weather(location, language)
    assert isinstance(model, language._model_)


def test_language_type_error(location: str) -> None:
    msg = "Invalid language 'en'. Must be a member of pywttr.Language enum."
    with pytest.raises(TypeError, match=msg):
        pywttr.get_weather(location, "en")  # type: ignore[call-overload]
