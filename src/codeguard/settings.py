"""Environment-backed settings for the Week 2 baseline."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _load_local_env(path: Path = Path(".env")) -> None:
    """Load simple KEY=VALUE pairs without adding another runtime dependency."""
    if not path.is_file():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_local_env()


def _read_float(name: str, default: float) -> float:
    raw = os.getenv(name, "").strip()
    return float(raw) if raw else default


def _read_int(name: str, default: int) -> int:
    raw = os.getenv(name, "").strip()
    return int(raw) if raw else default


@dataclass(frozen=True)
class Settings:
    """Runtime configuration with safe defaults and no embedded secrets."""

    provider: str = os.getenv("MODEL_PROVIDER", "gemini").strip() or "gemini"
    model_name: str = (
        os.getenv("MODEL_NAME", "gemini-3.1-flash-lite").strip()
        or "gemini-3.1-flash-lite"
    )
    prompt_version: str = os.getenv("PROMPT_VERSION", "v1.1").strip() or "v1.1"
    temperature: float = _read_float("MODEL_TEMPERATURE", 0.2)
    max_output_tokens: int = _read_int("MODEL_MAX_OUTPUT_TOKENS", 4096)

    def validate(self) -> None:
        if self.provider not in {"gemini", "mock"}:
            raise ValueError("MODEL_PROVIDER must be 'gemini' or 'mock'.")
        if self.prompt_version not in {"v1.0", "v1.1"}:
            raise ValueError("PROMPT_VERSION must be 'v1.0' or 'v1.1'.")
        if not 0.0 <= self.temperature <= 1.0:
            raise ValueError("MODEL_TEMPERATURE must be between 0 and 1.")
        if not 256 <= self.max_output_tokens <= 8192:
            raise ValueError("MODEL_MAX_OUTPUT_TOKENS must be between 256 and 8192.")
