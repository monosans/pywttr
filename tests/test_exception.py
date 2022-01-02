# -*- coding: utf-8 -*-
import pytest
from requests.exceptions import HTTPError

import pywttr


def test_validation() -> None:
    location = "sdlaghdsaklgthj"
    with pytest.raises(HTTPError):
        pywttr.en.get_forecast(location)
