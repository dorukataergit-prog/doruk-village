from pathlib import Path
import os
import re
import shlex
import subprocess
from typing import Iterable

from backend.config import ROOT, WORKSPACE_DIR, ALLOWED_ENV_VARS

BLOCK_PATTERNS = [
    "rm -rf /",
    "sudo ",
    "chmod -R",
    "chown",
    "curl ",
    "wget ",
    "nc ",
    "ncat ",
    "ssh ",
    "scp ",
    "openssl enc",
    "> /",
    "< /",
    "/etc/passwd",
    "/proc/",
    "LD_PRELOAD",
    "env ",
    "export ",
    "unset ",
]


class SafePathPolicy:
    @staticmethod
    def resolve(path: str) -> Path:
        candidate = Path(path)
        if candidate.is_absolute():
            if not str(candidate).startswith(str(WORKSPACE_DIR)):
                raise ValueError(f"Access outside workspace is blocked: {path}")
            return candidate.resolve()
        return (WORKSPACE_DIR / candidate).resolve()

    @staticmethod
    def validate(path: str) -> Path:
        resolved = SafePathPolicy.resolve(path)
        if ".." in Path(path).parts:
            raise ValueError(f"Path traversal is blocked: {path}")
        if not str(resolved).startswith(str(WORKSPACE_DIR.resolve())):
            raise ValueError(f"Access outside workspace is blocked: {path}")
        return resolved


class CommandPolicy:
    @staticmethod
    def validate(command: str) -> None:
        if not command or not command.strip():
            raise ValueError("Empty command is not allowed.")
        lowered = command.lower()
        for pattern in BLOCK_PATTERNS:
            if pattern in lowered:
                raise ValueError(f"Blocked command pattern: {pattern}")
        if ".." in command and not command.startswith("git "):
            raise ValueError("Directory traversal is blocked in commands.")

    @staticmethod
    def safe_tokens(command: str):
        CommandPolicy.validate(command)
        return shlex.split(command)


class SecretGuard:
    @staticmethod
    def read_environment(name: str):
        if name not in ALLOWED_ENV_VARS:
            raise PermissionError(f"Reading environment variable '{name}' is blocked.")
        return os.getenv(name)


def ensure_workspace_root(path: Path) -> Path:
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    return path
