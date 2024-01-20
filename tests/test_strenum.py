from __future__ import annotations

from enum import auto

import pytest
from pywttr_models._strenum import StrEnum  # noqa: PLC2701


class Foo(StrEnum):
    BAR = auto()
    baz = auto()


@pytest.mark.parametrize("member", Foo)
def test_generate_next_value(member: Foo) -> None:
    assert member._name_ == member._value_ == str(member)
