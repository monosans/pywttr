from __future__ import annotations

from enum import auto

from pywttr_models._strenum import StrEnum


def test_generate_next_value() -> None:
    class Foo(StrEnum):
        BAR = auto()
        baz = auto()

    for member in Foo:
        assert member.name == member.value
