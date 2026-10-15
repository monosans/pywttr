"""Wrapper for the [wttr.in](https://wttr.in) weather API.

Examples:
    ```python
    import pywttr

    with pywttr.Wttr() as wttr:
        weather = wttr.weather("Paris")
    print(weather.current_condition[0].temp_c)
    ```
"""

from __future__ import annotations

import pywttr_models as models
from pywttr_models._language import Language  # noqa: PLC2701

from pywttr._wttr import Wttr

__version__ = "4.0.5"
__all__ = ("Language", "Wttr", "models")
