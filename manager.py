class BenchmarkDatasetManager:
    """Interface for reference, challenge, and synthetic anomaly datasets."""
    def __init__(self):
        self.datasets = {}

    def register(self, name, dataset, category):
        if category not in {"reference", "challenge", "synthetic"}:
            raise ValueError("category must be reference, challenge, or synthetic")
        self.datasets[name] = {"dataset": dataset, "category": category}
