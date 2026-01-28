from config.config_loader import load_config

if __name__ == "__main__":
    cfg = load_config()
    print("Experiment name:", cfg["experiment"]["experiment"]["name"])
    print("Primary metric:", cfg["metrics"]["metrics"]["primary"]["name"])
