# -*- coding: utf-8 -*-
from typing import Any as _Any
from typing import Optional as _Optional

from requests import Session as _Session


def _fetch(location: str, session: _Session, lang: str) -> _Any:
    with session.get(
        f"https://wttr.in/{location}", params={"format": "j1", "lang": lang}
    ) as r:
        r.raise_for_status()
        return r.json()


def get_json(location: str, session: _Optional[_Session], lang: str) -> _Any:
    if session:
        return _fetch(location, session, lang)
    with _Session() as session:
        return _fetch(location, session, lang)
