from __future__ import annotations

from typing import Optional

import pywttr_models
from pywttr_models._language import Language
from requests import Session
from typing_extensions import Literal, overload

from ._http import get_json


@overload
def get_weather(
    location: str,
    language: Literal[Language.AF],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.af.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.AM],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.am.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.AR],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.ar.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.BE],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.be.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.BN],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.bn.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.CA],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.ca.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.DA],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.da.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.DE],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.de.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.EL],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.el.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.EN] = ...,
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.en.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.ET],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.et.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.FA],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.fa.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.FR],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.fr.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.GL],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.gl.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.HI],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.hi.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.HU],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.hu.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.IA],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.ia.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.ID],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.id.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.IT],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.it.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.LT],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.lt.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.MG],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.mg.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.NB],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.nb.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.NL],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.nl.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.OC],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.oc.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.PL],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.pl.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.PT_BR],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.pt_br.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.RO],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.ro.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.RU],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.ru.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.TA],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.ta.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.TH],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.th.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.TR],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.tr.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.UK],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.uk.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.VI],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.vi.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.ZH_CN],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.zh_cn.Model:
    ...


@overload
def get_weather(
    location: str,
    language: Literal[Language.ZH_TW],
    *,
    session: Optional[Session] = ...,
) -> pywttr_models.zh_tw.Model:
    ...


@overload
def get_weather(
    location: str, language: Language, *, session: Optional[Session] = ...
) -> pywttr_models.AnyModel:
    ...


def get_weather(
    location: str,
    language: Language = Language.EN,
    *,
    session: Optional[Session] = None,
) -> pywttr_models.AnyModel:
    """Wrapper for wttr.in weather API.

    Examples:
        Prints the average temperature in Paris today:

        ```python
        import pywttr

        # Choose language. First option is preferred for typing.
        language = pywttr.Language.ZH_CN
        language = pywttr.Language["ZH_CN"]
        language = pywttr.Language("zh-cn")
        weather = pywttr.get_weather("Paris", language)
        print(weather.weather[0].avgtemp_c)
        ```
    """
    try:
        model = language._model_
        lang = language._value_
    except AttributeError as e:
        msg = (
            f"Invalid language {language!r}. "
            "Must be a member of pywttr.Language enum."
        )
        raise TypeError(msg) from e
    response = get_json(location, lang, session)
    return model.parse_obj(response)
