from weather_eval.statistical_tests.metrics import compute_bias

def test_compute_bias():
    assert compute_bias([2, 4], [1, 3]) == 1.0
