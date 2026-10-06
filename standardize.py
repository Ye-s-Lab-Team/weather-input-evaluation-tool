import pandas as pd
from weather_eval.models import WeatherDataset

def standardize_input(df: pd.DataFrame, metadata: dict | None = None) -> WeatherDataset:
    """Month-2 interface for canonical input standardization.

    Detailed variable mappings, units, and time-resolution rules will be
    finalized as Tasks 1.0/1.3 mature.
    """
    data = df.copy()
    data.columns = [str(c).strip().lower() for c in data.columns]
    return WeatherDataset(data=data, metadata=metadata or {})
