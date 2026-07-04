from pathlib import Path

# Resolve project root relative to this file so paths work regardless of CWD
PROJECT_ROOT = Path(__file__).resolve().parents[3]

CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"

