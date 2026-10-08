from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_DIR = ROOT / "workspace"
AGENTS_DIR = ROOT / "agents"
LOGS_DIR = ROOT / "logs"
TASKS_DIR = ROOT / "tasks"
BENCHMARKS_DIR = ROOT / "benchmarks"
FRONTEND_DIR = ROOT / "frontend"
APP_ENV_FILE = ROOT / ".env"

ALLOWED_ENV_VARS = {
    "NVIDIA_API_KEY",
    "NVIDIA_MODEL",
    "PYTHONPATH",
    "PATH",
}


def load_env():
    from dotenv import load_dotenv

    if APP_ENV_FILE.exists():
        load_dotenv(APP_ENV_FILE)


load_env()
