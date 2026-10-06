import numpy as np

def compute_bias(candidate, reference):
    c = np.asarray(candidate, dtype=float)
    r = np.asarray(reference, dtype=float)
    if c.shape != r.shape:
        raise ValueError("candidate and reference must have the same shape")
    return float(np.nanmean(c - r))

def compare_distributions(candidate, reference):
    """Placeholder interface; statistical test selection is a Task 1.3 decision."""
    raise NotImplementedError

def evaluate_extremes(series):
    """Placeholder interface; extreme-value rules are a Task 1.3 decision."""
    raise NotImplementedError
