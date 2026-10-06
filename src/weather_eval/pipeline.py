from weather_eval.models import EvaluationReport

def evaluate_weather_dataset(dataset, benchmark=None, config=None):
    """Top-level Month-2 orchestration interface.

    Method modules are intentionally not hard-coded yet. They will be added
    after Task 1.0 user requirements and Task 1.3 method selection/PMS review.
    """
    return EvaluationReport(metadata={
        "status": "framework scaffold",
        "benchmark_attached": benchmark is not None,
    })
