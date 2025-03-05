from __future__ import annotations

from typing import Final, Optional

import pywttr_models
from httpx import Client, Timeout
from pydantic import AnyHttpUrl, validate_call
from pywttr_models._language import Language  # noqa: PLC2701
from typing_extensions import Literal, Self, final, overload


@final
class Wttr:
    """Wrapper for wttr.in weather API.

    Examples:
        Choose language. First option is preferred because of type safety.

        ```python
        language = pywttr.Language.ZH_CN
        language = pywttr.Language["ZH_CN"]
        language = pywttr.Language("zh-cn")
        ```

        Print the average temperature in Paris today:

        ```python
        with pywttr.Wttr() as wttr:
            weather = wttr.weather("Paris", language=language)
        print(weather.weather[0].avgtemp_c)
        ```

        Custom base url:

        ```python
        with pywttr.Wttr(
            base_url=pydantic.AnyHttpUrl("https://example.com")
        ) as wttr:
            ...
        ```

        Custom httpx.Client:

        ```python
        with httpx.Client(
            timeout=httpx.Timeout(60, connect=5), follow_redirects=True
        ) as session:
            wttr = pywttr.Wttr(session=session)
            ...
        ```
    """

    __slots__ = ("_base_url", "_session")

    @validate_call(config={"arbitrary_types_allowed": True})
    def __init__(
        self,
        *,
        base_url: AnyHttpUrl = AnyHttpUrl.build(  # noqa: B008
            scheme="https", host="wttr.in"
        ),
        session: Optional[Client] = None,
    ) -> None:
        self._base_url: Final = base_url
        self._session = session

    @property
    def base_url(self) -> AnyHttpUrl:
        return self._base_url

    @property
    def session(self) -> Optional[Client]:
        return self._session

    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.AF]
    ) -> pywttr_models.af.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.AM]
    ) -> pywttr_models.am.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.AR]
    ) -> pywttr_models.ar.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.BE]
    ) -> pywttr_models.be.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.BN]
    ) -> pywttr_models.bn.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.CA]
    ) -> pywttr_models.ca.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.DA]
    ) -> pywttr_models.da.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.DE]
    ) -> pywttr_models.de.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.EL]
    ) -> pywttr_models.el.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.EN] = ...
    ) -> pywttr_models.en.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.ET]
    ) -> pywttr_models.et.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.FA]
    ) -> pywttr_models.fa.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.FR]
    ) -> pywttr_models.fr.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.GL]
    ) -> pywttr_models.gl.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.HI]
    ) -> pywttr_models.hi.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.HU]
    ) -> pywttr_models.hu.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.IA]
    ) -> pywttr_models.ia.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.ID]
    ) -> pywttr_models.id.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.IT]
    ) -> pywttr_models.it.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.LT]
    ) -> pywttr_models.lt.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.MG]
    ) -> pywttr_models.mg.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.NB]
    ) -> pywttr_models.nb.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.NL]
    ) -> pywttr_models.nl.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.OC]
    ) -> pywttr_models.oc.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.PL]
    ) -> pywttr_models.pl.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.PT_BR]
    ) -> pywttr_models.pt_br.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.RO]
    ) -> pywttr_models.ro.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.RU]
    ) -> pywttr_models.ru.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.TA]
    ) -> pywttr_models.ta.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.TH]
    ) -> pywttr_models.th.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.TR]
    ) -> pywttr_models.tr.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.UK]
    ) -> pywttr_models.uk.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.VI]
    ) -> pywttr_models.vi.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.ZH_CN]
    ) -> pywttr_models.zh_cn.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Literal[Language.ZH_TW]
    ) -> pywttr_models.zh_tw.Model: ...
    @overload
    def weather(
        self, location: str, /, *, language: Language
    ) -> pywttr_models.AnyModel: ...

    @validate_call(config={"arbitrary_types_allowed": True})
    def weather(
        self, location: str, /, *, language: Language = Language.EN
    ) -> pywttr_models.AnyModel:
        """Wrapper for wttr.in weather API.

        Examples:
            Choose language. First option is preferred because of type safety.

            ```python
            language = pywttr.Language.ZH_CN
            language = pywttr.Language["ZH_CN"]
            language = pywttr.Language("zh-cn")
            ```

            Print the average temperature in Paris today:

            ```python
            with pywttr.Wttr() as wttr:
                weather = wttr.weather("Paris", language=language)
            print(weather.weather[0].avgtemp_c)
            ```

            Custom base url:

            ```python
            with pywttr.Wttr(
                base_url=pydantic.AnyHttpUrl("https://example.com")
            ) as wttr:
                ...
            ```

            Custom httpx.Client:

            ```python
            with httpx.Client(
                timeout=httpx.Timeout(60, connect=5), follow_redirects=True
            ) as session:
                wttr = pywttr.Wttr(session=session)
                ...
            ```
        """
        if self._session is None:
            self._session = Client(
                timeout=Timeout(60, connect=5), follow_redirects=True
            )
        response = self._session.get(
            f"{self._base_url}/{location}",
            params={"format": "j1", "lang": language},
            headers={"Accept": "application/json"},
        )
        response.raise_for_status()
        return language._model_.model_validate_json(response.content)

    def close(self) -> None:
        """Close HTTP session."""
        if self._session is not None:
            self._session.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
