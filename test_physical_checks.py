from weather_eval.physical_consistency.checks import (
    check_dewpoint_not_above_drybulb, check_relative_humidity_bounds
)

def test_dewpoint_rule_passes():
    assert check_dewpoint_not_above_drybulb([20, 10], [15, 8]).passed

def test_dewpoint_rule_fails():
    assert not check_dewpoint_not_above_drybulb([20], [21]).passed

def test_rh_bounds():
    assert check_relative_humidity_bounds([0, 50, 100]).passed
    assert not check_relative_humidity_bounds([101]).passed
