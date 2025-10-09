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

from __future__ import annotations

import pywttr_models as models
from pywttr_models._language import Language  # noqa: PLC2701

from pywttr._wttr import Wttr

__version__ = "4.0.1"
__all__ = ("Language", "Wttr", "models")
