# pywttr

[![CI](https://github.com/monosans/pywttr/actions/workflows/ci.yml/badge.svg)](https://github.com/monosans/pywttr/actions/workflows/ci.yml)
[![Downloads](https://static.pepy.tech/badge/pywttr)](https://pepy.tech/project/pywttr)

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

## License

[MIT](https://github.com/monosans/pywttr/blob/main/LICENSE)
