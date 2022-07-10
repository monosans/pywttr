from __future__ import annotations

import pytest
from requests.exceptions import HTTPError

from pywttr import Wttr


def test_exception() -> None:
    wttr = Wttr("sdlaghdsaklgthj")
    with pytest.raises(HTTPError):
        wttr.en()
