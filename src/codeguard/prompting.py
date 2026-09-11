"""Versioned prompt loading and construction."""

from __future__ import annotations

from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SUPPORTED_PROMPTS = {"v1.0", "v1.1"}


def prompt_path(version: str) -> Path:
    if version not in SUPPORTED_PROMPTS:
        raise ValueError(f"Unsupported prompt version: {version}")
    return REPOSITORY_ROOT / "prompts" / version / "test-plan.md"


def build_prompt(*, feature: str, requirements: str, version: str) -> str:
    feature = feature.strip()
    requirements = requirements.strip()
    if not feature:
        raise ValueError("Feature must not be blank.")

    template = prompt_path(version).read_text(encoding="utf-8")
    return (
        template.replace("{{FEATURE}}", feature)
        .replace("{{REQUIREMENTS}}", requirements or "NO REQUIREMENTS PROVIDED")
    )