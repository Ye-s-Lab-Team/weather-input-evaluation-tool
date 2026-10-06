import numpy as np
from weather_eval.models import CheckResult

def check_dewpoint_not_above_drybulb(dry_bulb, dew_point):
    db = np.asarray(dry_bulb, dtype=float)
    dp = np.asarray(dew_point, dtype=float)
    ok = bool(np.all((np.isnan(db) | np.isnan(dp)) | (dp <= db)))
    return CheckResult("dewpoint_not_above_drybulb", ok, message="Dew point should not exceed dry-bulb temperature.")

def check_relative_humidity_bounds(relative_humidity):
    rh = np.asarray(relative_humidity, dtype=float)
    ok = bool(np.all(np.isnan(rh) | ((rh >= 0) & (rh <= 100))))
    return CheckResult("relative_humidity_bounds", ok, message="Relative humidity expected within 0-100%.")

def check_wind_speed_nonnegative(wind_speed):
    ws = np.asarray(wind_speed, dtype=float)
    ok = bool(np.all(np.isnan(ws) | (ws >= 0)))
    return CheckResult("wind_speed_nonnegative", ok, message="Wind speed should be non-negative.")
