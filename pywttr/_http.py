from __future__ import annotations

from typing import Optional

from requests import Response, Session
from typing_extensions import Any


def get_json(location: str, language: str, session: Optional[Session]) -> Any:
    if isinstance(session, Session):
        response = fetch(location, language, session)
    else:
        with Session() as session:  # noqa: PLR1704
            response = fetch(location, language, session)
    response.raise_for_status()
    return response.json()


def fetch(location: str, language: str, session: Session) -> Response:
    with session.get(
        f"https://wttr.in/{location}",
        params={"format": "j1", "lang": language},
        headers={"Accept": "application/json"},
    ) as response:
        return response
