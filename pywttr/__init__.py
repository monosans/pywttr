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
from __future__ import annotations

import pywttr_models as models
from pywttr_models._language import Language

from ._get_weather import get_weather
from ._wttr import Wttr, WttrClassDeprecationWarning

__all__ = (
    "models",
    "Language",
    "get_weather",
    "Wttr",
    "WttrClassDeprecationWarning",
)
