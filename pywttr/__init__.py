"""Wrapper for wttr.in weather forecast API."""
from __future__ import annotations

import pywttr_models as models

from ._wttr import Wttr

__all__ = ("Wttr", "models")
