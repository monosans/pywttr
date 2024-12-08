from __future__ import annotations

import pytest

import pywttr


@pytest.mark.parametrize("language", pywttr.Language)
def test_language_value(language: pywttr.Language) -> None:
    assert language._name_ == language._value_.replace("-", "_").upper()


@pytest.mark.parametrize("language", pywttr.Language)
def test_language_model(language: pywttr.Language) -> None:
    assert (
        language._model_
        is getattr(pywttr.models, language._name_.lower()).Model
    )


def test_language_str() -> None:
    assert pywttr.Language.EN._value_ == str(pywttr.Language.EN)
