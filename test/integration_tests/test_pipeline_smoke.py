import pandas as pd
from weather_eval.input_standardization.standardize import standardize_input
from weather_eval.pipeline import evaluate_weather_dataset

def test_pipeline_smoke():
    ds = standardize_input(pd.DataFrame({"Dry Bulb": [20.0]}), {"source": "test"})
    report = evaluate_weather_dataset(ds)
    assert report.metadata["status"] == "framework scaffold"
