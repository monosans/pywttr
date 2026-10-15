# Guide

Every example is a complete script: copy it and run it.

## What's in a response

[`Wttr.weather`][pywttr.Wttr.weather] returns a [`Model`][pywttr.models.base.Model]:

- `current_condition[0]`: the weather now ([`CurrentConditionItem`][pywttr.models.base.CurrentConditionItem]).
- `weather[0]` to `weather[2]`: today, tomorrow and the day after ([`WeatherItem`][pywttr.models.base.WeatherItem]).
- `weather[i].hourly`: that day in 3-hour steps ([`HourlyItem`][pywttr.models.base.HourlyItem]).
- `weather[i].astronomy[0]`: sunrise, sunset and the moon ([`AstronomyItem`][pywttr.models.base.AstronomyItem]).
- `nearest_area[0]`: the place wttr.in found ([`NearestAreaItem`][pywttr.models.base.NearestAreaItem]).

Most values come in metric and imperial units, e.g. `temp_c` and `temp_f`.

## Current weather

```python
import pywttr

with pywttr.Wttr() as wttr:
    weather = wttr.weather("London")

now = weather.current_condition[0]
print(f"{now.temp_c} °C, feels like {now.feels_like_c} °C")
print(now.weather_desc[0].value)
print(f"Wind {now.windspeed_kmph} km/h {now.winddir16_point}")
```

## Forecast for tomorrow

`weather[1]` is tomorrow, `weather[2]` is the day after.

```python
import pywttr

with pywttr.Wttr() as wttr:
    weather = wttr.weather("Tokyo")

tomorrow = weather.weather[1]
print(tomorrow.date, f"{tomorrow.mintemp_c}..{tomorrow.maxtemp_c} °C")
print("Sunrise:", tomorrow.astronomy[0].sunrise)
```

## Hourly forecast

`hourly` has 8 items, from 00:00 to 21:00 local time. [`time`][pywttr.models.base.HourlyItem.time] is a number: `0`, `300`, ..., `2100`.

```python
import pywttr

with pywttr.Wttr() as wttr:
    weather = wttr.weather("Berlin")

for hour in weather.weather[0].hourly:
    time = f"{hour.time // 100:02}:00"
    print(time, f"{hour.temp_c} °C", f"rain {hour.chanceofrain}%")
```

## Several locations

wttr.in accepts cities, coordinates, airport codes and landmarks after `~`. Reuse one [`Wttr`][pywttr.Wttr] for many requests: it keeps the connection open.

```python
import pywttr

locations = ["Paris", "48.8567,2.3508", "CDG", "~Eiffel Tower"]

with pywttr.Wttr() as wttr:
    for location in locations:
        area = wttr.weather(location).nearest_area[0]
        print(location, "->", area.area_name[0].value, area.country[0].value)
```

## Weather in another language

Pass a [`Language`][pywttr.Language]. The translated description is in `lang_<code>`, e.g. `lang_fr`; `weather_desc` stays in English.

```python
import pywttr

with pywttr.Wttr() as wttr:
    weather = wttr.weather("Paris", language=pywttr.Language.FR)

now = weather.current_condition[0]
print(now.lang_fr[0].value)
print(now.weather_desc[0].value)
```

If the language is only known at runtime, e.g. `pywttr.Language("fr")`, read `lang_xx`: every model has it.

## Custom HTTP client and timeouts

Pass your own [`httpx2.Client`][httpx2.Client] to change timeouts, proxies or headers. The default client has a 60 s timeout (5 s to connect).

```python
import httpx2
import pywttr

with httpx2.Client(timeout=30, follow_redirects=True) as client:
    wttr = pywttr.Wttr(session=client)
    weather = wttr.weather("Oslo")

print(weather.current_condition[0].temp_c)
```

!!! warning

    [`Wttr.close`][pywttr.Wttr.close] closes the client you passed, and leaving `with pywttr.Wttr(...)` calls it.

## Self-hosted wttr.in

Point `base_url` at your own [wttr.in server](https://github.com/chubin/wttr.in).

```python
import pydantic
import pywttr

base_url = pydantic.AnyHttpUrl("https://wttr.example.com")

with pywttr.Wttr(base_url=base_url) as wttr:
    weather = wttr.weather("Paris")

print(weather.current_condition[0].temp_c)
```

## Handling errors

wttr.in answers an unknown location with an error status, which raises [`httpx2.HTTPStatusError`][httpx2.HTTPStatusError]. Network errors and timeouts raise other [`httpx2.HTTPError`][httpx2.HTTPError] subclasses.

```python
import httpx2
import pywttr

with pywttr.Wttr() as wttr:
    try:
        weather = wttr.weather("qwertyuiopasdf")
    except httpx2.HTTPStatusError as e:
        print("wttr.in error:", e.response.status_code)
    except httpx2.HTTPError as e:
        print("Network error:", e)
    else:
        print(weather.current_condition[0].temp_c)
```
