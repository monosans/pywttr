# pywttr

[![CI](https://github.com/monosans/pywttr/actions/workflows/ci.yml/badge.svg)](https://github.com/monosans/pywttr/actions/workflows/ci.yml)
[![Downloads](https://static.pepy.tech/badge/pywttr)](https://pepy.tech/project/pywttr)

Wrapper for [wttr.in](https://wttr.in) weather API.

Asynchronous version [here](https://github.com/monosans/aiopywttr).

## Installation

```bash
pip install -U pywttr pywttr-models
```

## Documentation

<https://pywttr.readthedocs.io>

## Simple example

```python
with pywttr.Wttr() as wttr:
    weather = wttr.weather("Paris", language=pywttr.Language.EN)
print(weather.weather[0].avgtemp_c)
```

## License

[MIT](https://github.com/monosans/pywttr/blob/main/LICENSE)
