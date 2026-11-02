# API reference

::: pywttr.Wttr
    options:
      members:
        - weather
        - close
        - base_url
        - session
        - __enter__
        - __exit__

## Language

::: pywttr.Language
    options:
      heading_level: 4
      show_attribute_values: false
      show_labels: false
      show_root_heading: false

## Response models

Each language has its own module, such as `pywttr.models.fr`. Its `CurrentConditionItem` and `HourlyItem` add the translated description twice: as `lang_fr` and as `lang_xx`, which every language has.

::: pywttr.models.base
    options:
      heading_level: 3
      members:
        - Model
        - CurrentConditionItem
        - WeatherItem
        - HourlyItem
        - AstronomyItem
        - NearestAreaItem
        - RequestItem
        - WeatherDescItem
        - WeatherIconUrlItem
        - AreaNameItem
        - CountryItem
        - RegionItem
        - WeatherUrlItem
        - LangItem
      show_attribute_values: false
      show_labels: false
      show_root_heading: false
      show_root_toc_entry: false

::: pywttr.models.AnyModel
    options:
      heading_level: 3
      show_attribute_values: false
      show_labels: false
