# pywttr

[![Downloads](https://static.pepy.tech/badge/pywttr)](https://pepy.tech/project/pywttr)

Wrapper for [wttr.in](https://wttr.in) weather API.

Asynchronous version [here](https://github.com/monosans/aiopywttr).

## Installation

```bash
pip install -U pywttr pywttr-models
```

## Documentation

<https://monosans.github.io/pywttr>

## Simple example

```python
with pywttr.Wttr() as wttr:
    weather = wttr.weather("Paris", language=pywttr.Language.EN)
print(weather.weather[0].avgtemp_c)
```

## License

[MIT](https://github.com/monosans/pywttr/blob/main/LICENSE)
