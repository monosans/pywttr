# pywttr

[![CI](https://github.com/monosans/pywttr/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/monosans/pywttr/actions/workflows/ci.yml?query=event%3Apush+branch%3Amain)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/monosans/pywttr/main.svg)](https://results.pre-commit.ci/latest/github/monosans/pywttr/main)
[![Coverage](https://img.shields.io/codecov/c/github/monosans/pywttr/main?logo=codecov)](https://codecov.io/gh/monosans/pywttr)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pywttr?logo=pypi)](https://pypi.org/project/pywttr/)

Wrapper for [wttr.in](https://wttr.in) weather forecast API.

Asynchronous version [here](https://github.com/monosans/aiopywttr).

## Installation

```bash
python -m pip install -U pywttr pywttr-models
```

## Example

This example prints the average temperature in New York today.

```python
import pywttr

wttr = pywttr.Wttr("New York")
forecast = wttr.en()
print(forecast.weather[0].avgtemp_c)
```

Other languages may also be used instead of `en`. For a complete list of supported languages, follow the code completion in your IDE.

## Documentation

There is no documentation, just follow the example and code completion in your IDE.

All types of objects returned by the wttr.in API are in the `pywttr.models` package.

## Recommended IDEs

- [Visual Studio Code](https://code.visualstudio.com) (with [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python))
- [PyCharm](https://jetbrains.com/pycharm)

## License

[MIT](https://github.com/monosans/pywttr/blob/main/LICENSE)
