<img src="https://raw.githubusercontent.com/monosans/pywttr/main/docs/assets/logo.svg" alt="" width="96" align="right">

# pywttr

[![Downloads](https://static.pepy.tech/badge/pywttr)](https://pepy.tech/project/pywttr)

Typed Python client for the [wttr.in](https://wttr.in) weather API. For asyncio, use [aiopywttr](https://github.com/monosans/aiopywttr).

## Installation

```bash
uv add pywttr pywttr-models
# or
pip install -U pywttr pywttr-models
```

## Example

```python
import pywttr

with pywttr.Wttr() as wttr:
    weather = wttr.weather("Paris")

now = weather.current_condition[0]
print(f"{now.temp_c} °C, {now.weather_desc[0].value}")
```

## Documentation

<https://monosans.github.io/pywttr>

## License

[MIT](https://github.com/monosans/pywttr/blob/main/LICENSE)
