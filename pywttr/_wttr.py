# -*- coding: utf-8 -*-
from typing import Any, Optional

import pywttr_models
from requests import Session


class Wttr:
    """Wrapper for wttr.in weather forecast."""

    def __init__(
        self, location: str, *, session: Optional[Session] = None
    ) -> None:
        self.location = location
        self.session = session

    def af(self) -> pywttr_models.af.Model:
        return pywttr_models.af.Model.parse_obj(self._get_json("af"))

    def am(self) -> pywttr_models.am.Model:
        return pywttr_models.am.Model.parse_obj(self._get_json("am"))

    def ar(self) -> pywttr_models.ar.Model:
        return pywttr_models.ar.Model.parse_obj(self._get_json("ar"))

    def az(self) -> pywttr_models.az.Model:
        return pywttr_models.az.Model.parse_obj(self._get_json("az"))

    def be(self) -> pywttr_models.be.Model:
        return pywttr_models.be.Model.parse_obj(self._get_json("be"))

    def bg(self) -> pywttr_models.bg.Model:
        return pywttr_models.bg.Model.parse_obj(self._get_json("bg"))

    def bn(self) -> pywttr_models.bn.Model:
        return pywttr_models.bn.Model.parse_obj(self._get_json("bn"))

    def bs(self) -> pywttr_models.bs.Model:
        return pywttr_models.bs.Model.parse_obj(self._get_json("bs"))

    def ca(self) -> pywttr_models.ca.Model:
        return pywttr_models.ca.Model.parse_obj(self._get_json("ca"))

    def cs(self) -> pywttr_models.cs.Model:
        return pywttr_models.cs.Model.parse_obj(self._get_json("cs"))

    def cy(self) -> pywttr_models.cy.Model:
        return pywttr_models.cy.Model.parse_obj(self._get_json("cy"))

    def da(self) -> pywttr_models.da.Model:
        return pywttr_models.da.Model.parse_obj(self._get_json("da"))

    def de(self) -> pywttr_models.de.Model:
        return pywttr_models.de.Model.parse_obj(self._get_json("de"))

    def el(self) -> pywttr_models.el.Model:
        return pywttr_models.el.Model.parse_obj(self._get_json("el"))

    def en(self) -> pywttr_models.en.Model:
        return pywttr_models.en.Model.parse_obj(self._get_json("en"))

    def eo(self) -> pywttr_models.eo.Model:
        return pywttr_models.eo.Model.parse_obj(self._get_json("eo"))

    def es(self) -> pywttr_models.es.Model:
        return pywttr_models.es.Model.parse_obj(self._get_json("es"))

    def et(self) -> pywttr_models.et.Model:
        return pywttr_models.et.Model.parse_obj(self._get_json("et"))

    def eu(self) -> pywttr_models.eu.Model:
        return pywttr_models.eu.Model.parse_obj(self._get_json("eu"))

    def fa(self) -> pywttr_models.fa.Model:
        return pywttr_models.fa.Model.parse_obj(self._get_json("fa"))

    def fi(self) -> pywttr_models.fi.Model:
        return pywttr_models.fi.Model.parse_obj(self._get_json("fi"))

    def fr(self) -> pywttr_models.fr.Model:
        return pywttr_models.fr.Model.parse_obj(self._get_json("fr"))

    def fy(self) -> pywttr_models.fy.Model:
        return pywttr_models.fy.Model.parse_obj(self._get_json("fy"))

    def ga(self) -> pywttr_models.ga.Model:
        return pywttr_models.ga.Model.parse_obj(self._get_json("ga"))

    def he(self) -> pywttr_models.he.Model:
        return pywttr_models.he.Model.parse_obj(self._get_json("he"))

    def hi(self) -> pywttr_models.hi.Model:
        return pywttr_models.hi.Model.parse_obj(self._get_json("hi"))

    def hr(self) -> pywttr_models.hr.Model:
        return pywttr_models.hr.Model.parse_obj(self._get_json("hr"))

    def hu(self) -> pywttr_models.hu.Model:
        return pywttr_models.hu.Model.parse_obj(self._get_json("hu"))

    def hy(self) -> pywttr_models.hy.Model:
        return pywttr_models.hy.Model.parse_obj(self._get_json("hy"))

    def ia(self) -> pywttr_models.ia.Model:
        return pywttr_models.ia.Model.parse_obj(self._get_json("ia"))

    def id(self) -> pywttr_models.id.Model:
        return pywttr_models.id.Model.parse_obj(self._get_json("id"))

    def is_(self) -> pywttr_models.is_.Model:
        return pywttr_models.is_.Model.parse_obj(self._get_json("is"))

    def it(self) -> pywttr_models.it.Model:
        return pywttr_models.it.Model.parse_obj(self._get_json("it"))

    def ja(self) -> pywttr_models.ja.Model:
        return pywttr_models.ja.Model.parse_obj(self._get_json("ja"))

    def jv(self) -> pywttr_models.jv.Model:
        return pywttr_models.jv.Model.parse_obj(self._get_json("jv"))

    def kk(self) -> pywttr_models.kk.Model:
        return pywttr_models.kk.Model.parse_obj(self._get_json("kk"))

    def ko(self) -> pywttr_models.ko.Model:
        return pywttr_models.ko.Model.parse_obj(self._get_json("ko"))

    def lt(self) -> pywttr_models.lt.Model:
        return pywttr_models.lt.Model.parse_obj(self._get_json("lt"))

    def lv(self) -> pywttr_models.lv.Model:
        return pywttr_models.lv.Model.parse_obj(self._get_json("lv"))

    def mg(self) -> pywttr_models.mg.Model:
        return pywttr_models.mg.Model.parse_obj(self._get_json("mg"))

    def mk(self) -> pywttr_models.mk.Model:
        return pywttr_models.mk.Model.parse_obj(self._get_json("mk"))

    def mr(self) -> pywttr_models.mr.Model:
        return pywttr_models.mr.Model.parse_obj(self._get_json("mr"))

    def nb(self) -> pywttr_models.nb.Model:
        return pywttr_models.nb.Model.parse_obj(self._get_json("nb"))

    def nl(self) -> pywttr_models.nl.Model:
        return pywttr_models.nl.Model.parse_obj(self._get_json("nl"))

    def nn(self) -> pywttr_models.nn.Model:
        return pywttr_models.nn.Model.parse_obj(self._get_json("nn"))

    def oc(self) -> pywttr_models.oc.Model:
        return pywttr_models.oc.Model.parse_obj(self._get_json("oc"))

    def pl(self) -> pywttr_models.pl.Model:
        return pywttr_models.pl.Model.parse_obj(self._get_json("pl"))

    def pt(self) -> pywttr_models.pt.Model:
        return pywttr_models.pt.Model.parse_obj(self._get_json("pt"))

    def pt_br(self) -> pywttr_models.pt_br.Model:
        return pywttr_models.pt_br.Model.parse_obj(self._get_json("pt-br"))

    def ro(self) -> pywttr_models.ro.Model:
        return pywttr_models.ro.Model.parse_obj(self._get_json("ro"))

    def ru(self) -> pywttr_models.ru.Model:
        return pywttr_models.ru.Model.parse_obj(self._get_json("ru"))

    def sk(self) -> pywttr_models.sk.Model:
        return pywttr_models.sk.Model.parse_obj(self._get_json("sk"))

    def sl(self) -> pywttr_models.sl.Model:
        return pywttr_models.sl.Model.parse_obj(self._get_json("sl"))

    def sr(self) -> pywttr_models.sr.Model:
        return pywttr_models.sr.Model.parse_obj(self._get_json("sr"))

    def sr_lat(self) -> pywttr_models.sr_lat.Model:
        return pywttr_models.sr_lat.Model.parse_obj(self._get_json("sr-lat"))

    def sv(self) -> pywttr_models.sv.Model:
        return pywttr_models.sv.Model.parse_obj(self._get_json("sv"))

    def ta(self) -> pywttr_models.ta.Model:
        return pywttr_models.ta.Model.parse_obj(self._get_json("ta"))

    def te(self) -> pywttr_models.te.Model:
        return pywttr_models.te.Model.parse_obj(self._get_json("te"))

    def th(self) -> pywttr_models.th.Model:
        return pywttr_models.th.Model.parse_obj(self._get_json("th"))

    def tr(self) -> pywttr_models.tr.Model:
        return pywttr_models.tr.Model.parse_obj(self._get_json("tr"))

    def uk(self) -> pywttr_models.uk.Model:
        return pywttr_models.uk.Model.parse_obj(self._get_json("uk"))

    def uz(self) -> pywttr_models.uz.Model:
        return pywttr_models.uz.Model.parse_obj(self._get_json("uz"))

    def vi(self) -> pywttr_models.vi.Model:
        return pywttr_models.vi.Model.parse_obj(self._get_json("vi"))

    def zh(self) -> pywttr_models.zh.Model:
        return pywttr_models.zh.Model.parse_obj(self._get_json("zh"))

    def zh_cn(self) -> pywttr_models.zh_cn.Model:
        return pywttr_models.zh_cn.Model.parse_obj(self._get_json("zh-cn"))

    def zh_tw(self) -> pywttr_models.zh_tw.Model:
        return pywttr_models.zh_tw.Model.parse_obj(self._get_json("zh-tw"))

    def zu(self) -> pywttr_models.zu.Model:
        return pywttr_models.zu.Model.parse_obj(self._get_json("zu"))

    def _fetch(self, lang: str, session: Session) -> Any:
        with session.get(
            f"https://wttr.in/{self.location}",
            params={"format": "j1", "lang": lang},
        ) as r:
            r.raise_for_status()
            return r.json()

    def _get_json(self, lang: str) -> Any:
        if isinstance(self.session, Session):
            return self._fetch(lang, self.session)
        with Session() as session:
            return self._fetch(lang, session)
