from __future__ import annotations

import pywttr


def test_language() -> None:
    assert (
        pywttr.Language.ZH_CN
        is pywttr.Language["ZH_CN"]
        is pywttr.Language("zh-cn")
    )


def test_language_model() -> None:
    assert pywttr.Language.EN._model_ is pywttr.models.en.Model
