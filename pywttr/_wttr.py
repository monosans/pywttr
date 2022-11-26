from __future__ import annotations

from typing import Any, Optional

import pywttr_models
from requests import Session


# pylint: disable-next=too-many-public-methods
class Wttr:
    """Wrapper for wttr.in weather forecast API."""

    __slots__ = ("location", "session")

    def __init__(
        self, location: str, session: Optional[Session] = None
    ) -> None:
        self.location = location
        self.session = session

    # pylint: disable=invalid-name
    def af(self) -> pywttr_models.af.Model:
        return pywttr_models.af.Model.parse_obj(self._get_json("af"))

    def am(self) -> pywttr_models.am.Model:
        return pywttr_models.am.Model.parse_obj(self._get_json("am"))

    def ar(self) -> pywttr_models.ar.Model:
        return pywttr_models.ar.Model.parse_obj(self._get_json("ar"))

    def be(self) -> pywttr_models.be.Model:
        return pywttr_models.be.Model.parse_obj(self._get_json("be"))

    def bn(self) -> pywttr_models.bn.Model:
        return pywttr_models.bn.Model.parse_obj(self._get_json("bn"))

    def ca(self) -> pywttr_models.ca.Model:
        return pywttr_models.ca.Model.parse_obj(self._get_json("ca"))

    def da(self) -> pywttr_models.da.Model:
        return pywttr_models.da.Model.parse_obj(self._get_json("da"))

    def de(self) -> pywttr_models.de.Model:
        return pywttr_models.de.Model.parse_obj(self._get_json("de"))

    def el(self) -> pywttr_models.el.Model:
        return pywttr_models.el.Model.parse_obj(self._get_json("el"))

    def en(self) -> pywttr_models.en.Model:
        return pywttr_models.en.Model.parse_obj(self._get_json("en"))

    def et(self) -> pywttr_models.et.Model:
        return pywttr_models.et.Model.parse_obj(self._get_json("et"))

    def fa(self) -> pywttr_models.fa.Model:
        return pywttr_models.fa.Model.parse_obj(self._get_json("fa"))

    def fr(self) -> pywttr_models.fr.Model:
        return pywttr_models.fr.Model.parse_obj(self._get_json("fr"))

    def hi(self) -> pywttr_models.hi.Model:
        return pywttr_models.hi.Model.parse_obj(self._get_json("hi"))

    def hu(self) -> pywttr_models.hu.Model:
        return pywttr_models.hu.Model.parse_obj(self._get_json("hu"))

    def ia(self) -> pywttr_models.ia.Model:
        return pywttr_models.ia.Model.parse_obj(self._get_json("ia"))

    def id(self) -> pywttr_models.id.Model:
        return pywttr_models.id.Model.parse_obj(self._get_json("id"))

    def it(self) -> pywttr_models.it.Model:
        return pywttr_models.it.Model.parse_obj(self._get_json("it"))

    def lt(self) -> pywttr_models.lt.Model:
        return pywttr_models.lt.Model.parse_obj(self._get_json("lt"))

    def mg(self) -> pywttr_models.mg.Model:
        return pywttr_models.mg.Model.parse_obj(self._get_json("mg"))

    def nb(self) -> pywttr_models.nb.Model:
        return pywttr_models.nb.Model.parse_obj(self._get_json("nb"))

    def nl(self) -> pywttr_models.nl.Model:
        return pywttr_models.nl.Model.parse_obj(self._get_json("nl"))

    def oc(self) -> pywttr_models.oc.Model:
        return pywttr_models.oc.Model.parse_obj(self._get_json("oc"))

    def pl(self) -> pywttr_models.pl.Model:
        return pywttr_models.pl.Model.parse_obj(self._get_json("pl"))

    def pt_br(self) -> pywttr_models.pt_br.Model:
        return pywttr_models.pt_br.Model.parse_obj(self._get_json("pt-br"))

    def ro(self) -> pywttr_models.ro.Model:
        return pywttr_models.ro.Model.parse_obj(self._get_json("ro"))

    def ru(self) -> pywttr_models.ru.Model:
        return pywttr_models.ru.Model.parse_obj(self._get_json("ru"))

    def ta(self) -> pywttr_models.ta.Model:
        return pywttr_models.ta.Model.parse_obj(self._get_json("ta"))

    def th(self) -> pywttr_models.th.Model:
        return pywttr_models.th.Model.parse_obj(self._get_json("th"))

    def tr(self) -> pywttr_models.tr.Model:
        return pywttr_models.tr.Model.parse_obj(self._get_json("tr"))

    def uk(self) -> pywttr_models.uk.Model:
        return pywttr_models.uk.Model.parse_obj(self._get_json("uk"))

    def vi(self) -> pywttr_models.vi.Model:
        return pywttr_models.vi.Model.parse_obj(self._get_json("vi"))

    def zh_cn(self) -> pywttr_models.zh_cn.Model:
        return pywttr_models.zh_cn.Model.parse_obj(self._get_json("zh-cn"))

    def zh_tw(self) -> pywttr_models.zh_tw.Model:
        return pywttr_models.zh_tw.Model.parse_obj(self._get_json("zh-tw"))

    # pylint: enable=invalid-name
    def _fetch(self, lang: str, session: Session) -> Any:
        with session.get(
            f"https://wttr.in/{self.location}",
            params={"format": "j1", "lang": lang},
        ) as response:
            response.raise_for_status()
            return response.json()

    def _get_json(self, lang: str) -> Any:
        if isinstance(self.session, Session):
            return self._fetch(lang, self.session)
        with Session() as session:
            return self._fetch(lang, session)
