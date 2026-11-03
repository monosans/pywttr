from __future__ import annotations

import keyword
import re

import httpx2
import pytest

import pywttr


@pytest.mark.parametrize("language", pywttr.Language)
def test_language_value(language: pywttr.Language) -> None:
    assert language._name_ == language._value_.replace("-", "_").upper()


@pytest.mark.parametrize("language", pywttr.Language)
def test_language_model(language: pywttr.Language) -> None:
    name = language._name_.lower()
    # A keyword can't name a module, so `is` gets a trailing underscore.
    module = getattr(pywttr.models, f"{name}_" if keyword.iskeyword(name) else name)
    assert language._model_ is module.Model


def test_language_str() -> None:
    assert pywttr.Language.EN._value_ == str(pywttr.Language.EN)


def test_language_matches_wttr_in() -> None:
    """wttr.in names the languages it supports when asked for one it doesn't."""
    response = httpx2.get(
        "https://wttr.in/", params={"format": "j1", "lang": "invalid"}, timeout=60
    )
    supported = re.search(r"expected one of \[([^\]]*)\]", response.text)
    assert supported, response.text
    assert sorted(map(str, pywttr.Language)) == sorted(supported[1].split())
