from dataclasses import dataclass, field
from typing import Any
import pandas as pd

@dataclass
class WeatherDataset:
    data: pd.DataFrame
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class CheckResult:
    name: str
    passed: bool | None
    value: Any = None
    message: str = ""

@dataclass
class EvaluationReport:
    checks: list[CheckResult] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
