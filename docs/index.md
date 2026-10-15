# pywttr

Typed Python client for the [wttr.in](https://wttr.in) weather API. For asyncio, use [aiopywttr](https://monosans.github.io/aiopywttr).

## Installation

=== "uv"

    ```bash
    uv add pywttr pywttr-models
    ```

=== "pip"

    ```bash
    pip install -U pywttr pywttr-models
    ```

## Quick start

```python
import pywttr

with pywttr.Wttr() as wttr:
    weather = wttr.weather("Paris")

now = weather.current_condition[0]
print(f"{now.temp_c} °C, {now.weather_desc[0].value}")
```

## Next steps

- [Guide](guide.md): current weather, forecasts, languages, timeouts, errors.
- [API Reference](api.md): every class, method and response field.
