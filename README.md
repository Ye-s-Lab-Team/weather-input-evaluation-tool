# ASHRAE 1939-TRP Weather Evaluation Tool

Initial software infrastructure for Task 1.1 (Implementation Framework).

## Purpose
Provide a modular, reproducible framework for evaluating the validity, suitability, and appropriateness of weather time series used in building and HVAC analysis.

## Current status
Month-2 architecture scaffold. Detailed methods, scoring thresholds, benchmark datasets, and application-specific rules will be developed and validated under later project tasks and PMS review.

## Proposed pipeline
1. Load candidate weather data and metadata.
2. Standardize names, units, timestamps, temporal resolution, and metadata.
3. Run completeness and deterministic statistical/physical checks.
4. Evaluate time-series and spatio-temporal structure.
5. Optionally run benchmarked ML anomaly detection.
6. Aggregate transparent diagnostics into reporting/scoring outputs.

## Development principles
- Python-first implementation
- Modular source layout
- Version control and review before merging
- Unit, integration, benchmark, and regression tests
- Continuous integration through GitHub Actions
