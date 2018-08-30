from typing import Tuple, Callable, Union
from datetime import datetime, timedelta

from ts_forecasting_pipeline import ModelSpecs

from bvp.data.models.forecasting.generic.model_a import configure_specs
from bvp.data.models.assets import Asset
from bvp.data.models.markets import Market
from bvp.data.models.weather import WeatherSensor

# Set the latest generic model. This function returns ModelSpecs and an identifier.
latest_model: Callable[
    [
        Union[Asset, Market, WeatherSensor],
        datetime,
        datetime,
        Union[timedelta, Tuple[datetime, datetime]],
        timedelta,
    ],
    Tuple[ModelSpecs, str],
] = configure_specs