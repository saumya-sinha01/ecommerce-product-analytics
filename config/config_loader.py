import yaml
from pathlib import Path

def _read_yaml(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Missing config file: {p}")
    return yaml.safe_load(p.read_text())

def load_config() -> dict:
    return {
        "base": _read_yaml("config/base.yaml"),
        "experiment": _read_yaml("config/experiment.yaml"),
        "metrics": _read_yaml("config/metrics.yaml"),
        "logging": _read_yaml("config/logging.yaml"),
    }
