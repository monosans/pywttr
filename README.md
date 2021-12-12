# pywttr

[![Build Status](https://github.com/monosans/pywttr/workflows/test/badge.svg?branch=main&event=push)](https://github.com/monosans/pywttr/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/monosans/pywttr/branch/main/graph/badge.svg)](https://codecov.io/gh/monosans/pywttr)
[![Python Version](https://img.shields.io/pypi/pyversions/pywttr.svg)](https://pypi.org/project/pywttr/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/monosans/pywttr/blob/main/LICENSE)

Wrapper for [wttr.in](https://wttr.in) weather forecast.

Asynchronous version [here](https://github.com/monosans/aiopywttr).

## Installation

```bash
pip install pywttr
```

## Example

This example prints the average temperature in New York today.

```python
import pywttr

forecast = pywttr.en.get_forecast("New York")
print(forecast.weather[0].avgtemp_c)
```

Other languages may also be used instead of `en`. For a complete list of supported languages, see the [file names](https://github.com/monosans/pywttr/tree/main/pywttr) or follow the code completion in your IDE.

## Documentation

There is no documentation, just follow the code completion from your IDE. I'd recommend [Visual Studio Code](https://code.visualstudio.com) (with [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)) or [PyCharm](https://jetbrains.com/pycharm).
