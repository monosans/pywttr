from __future__ import annotations

from typing import Optional

import pywttr_models
from pywttr_models._language import Language
from requests import Session
from typing_extensions import deprecated

from ._get_weather import get_weather


class WttrClassDeprecationWarning(DeprecationWarning):
    pass


@deprecated(
    "Use get_weather function instead", category=WttrClassDeprecationWarning
)
class Wttr:
    """Wrapper for wttr.in weather API.

    !!! warning "Deprecated"
        Use [get_weather](.#pywttr.get_weather) function instead.

    Examples:
        Prints the average temperature in Paris today:

        ```python
        import pywttr

        wttr = pywttr.Wttr("Paris")
        weather = wttr.en()
        print(weather.weather[0].avgtemp_c)
        ```
    """

    __slots__ = ("location", "session")

    def __init__(
        self, location: str, session: Optional[Session] = None
    ) -> None:
        self.location = location
        self.session = session

    def af(self) -> pywttr_models.af.Model:
        return get_weather(self.location, Language.AF, session=self.session)

    def am(self) -> pywttr_models.am.Model:
        return get_weather(self.location, Language.AM, session=self.session)

    def ar(self) -> pywttr_models.ar.Model:
        return get_weather(self.location, Language.AR, session=self.session)

    def be(self) -> pywttr_models.be.Model:
        return get_weather(self.location, Language.BE, session=self.session)

    def bn(self) -> pywttr_models.bn.Model:
        return get_weather(self.location, Language.BN, session=self.session)

    def ca(self) -> pywttr_models.ca.Model:
        return get_weather(self.location, Language.CA, session=self.session)

    def da(self) -> pywttr_models.da.Model:
        return get_weather(self.location, Language.DA, session=self.session)

    def de(self) -> pywttr_models.de.Model:
        return get_weather(self.location, Language.DE, session=self.session)

    def el(self) -> pywttr_models.el.Model:
        return get_weather(self.location, Language.EL, session=self.session)

    def en(self) -> pywttr_models.en.Model:
        return get_weather(self.location, Language.EN, session=self.session)

    def et(self) -> pywttr_models.et.Model:
        return get_weather(self.location, Language.ET, session=self.session)

    def fa(self) -> pywttr_models.fa.Model:
        return get_weather(self.location, Language.FA, session=self.session)

    def fr(self) -> pywttr_models.fr.Model:
        return get_weather(self.location, Language.FR, session=self.session)

    def gl(self) -> pywttr_models.gl.Model:
        return get_weather(self.location, Language.GL, session=self.session)

    def hi(self) -> pywttr_models.hi.Model:
        return get_weather(self.location, Language.HI, session=self.session)

    def hu(self) -> pywttr_models.hu.Model:
        return get_weather(self.location, Language.HU, session=self.session)

    def ia(self) -> pywttr_models.ia.Model:
        return get_weather(self.location, Language.IA, session=self.session)

    def id(self) -> pywttr_models.id.Model:  # noqa: A003
        return get_weather(self.location, Language.ID, session=self.session)

    def it(self) -> pywttr_models.it.Model:
        return get_weather(self.location, Language.IT, session=self.session)

    def lt(self) -> pywttr_models.lt.Model:
        return get_weather(self.location, Language.LT, session=self.session)

    def mg(self) -> pywttr_models.mg.Model:
        return get_weather(self.location, Language.MG, session=self.session)

    def nb(self) -> pywttr_models.nb.Model:
        return get_weather(self.location, Language.NB, session=self.session)

    def nl(self) -> pywttr_models.nl.Model:
        return get_weather(self.location, Language.NL, session=self.session)

    def oc(self) -> pywttr_models.oc.Model:
        return get_weather(self.location, Language.OC, session=self.session)

    def pl(self) -> pywttr_models.pl.Model:
        return get_weather(self.location, Language.PL, session=self.session)

    def pt_br(self) -> pywttr_models.pt_br.Model:
        return get_weather(self.location, Language.PT_BR, session=self.session)

    def ro(self) -> pywttr_models.ro.Model:
        return get_weather(self.location, Language.RO, session=self.session)

    def ru(self) -> pywttr_models.ru.Model:
        return get_weather(self.location, Language.RU, session=self.session)

    def ta(self) -> pywttr_models.ta.Model:
        return get_weather(self.location, Language.TA, session=self.session)

    def th(self) -> pywttr_models.th.Model:
        return get_weather(self.location, Language.TH, session=self.session)

    def tr(self) -> pywttr_models.tr.Model:
        return get_weather(self.location, Language.TR, session=self.session)

    def uk(self) -> pywttr_models.uk.Model:
        return get_weather(self.location, Language.UK, session=self.session)

    def vi(self) -> pywttr_models.vi.Model:
        return get_weather(self.location, Language.VI, session=self.session)

    def zh_cn(self) -> pywttr_models.zh_cn.Model:
        return get_weather(self.location, Language.ZH_CN, session=self.session)

    def zh_tw(self) -> pywttr_models.zh_tw.Model:
        return get_weather(self.location, Language.ZH_TW, session=self.session)
