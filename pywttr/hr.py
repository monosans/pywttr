# -*- coding: utf-8 -*-
from typing import Optional as _Optional

import pywttr_models as _pywttr_models
from requests import Session as _Session

from pywttr.http import get_json as _get_json


def get_forecast(
    location: str, *, session: _Optional[_Session] = None
) -> _pywttr_models.hr.Model:
    return _pywttr_models.hr.Model(**_get_json(location, session, "hr"))
