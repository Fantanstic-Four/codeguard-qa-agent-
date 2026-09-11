"""Command-line interface for the CodeGuard Week 2 baseline."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from pydantic import ValidationError

from codeguard.model_client import create_model_client
from codeguard.service import TestPlanService
from codeguard.settings import Settings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="codeguard",
        description="Generate a structured test plan from approved requirements.",
    )
    parser.add_argument("--feature", required=True, help="Feature being tested")
    parser.add_argument(
        "--requirements",
        required=True,
        type=Path,
        help="Path to an approved requirements text or Markdown file",
    )
    parser.add_argument(
        "--prompt-version",
        choices=["v1.0", "v1.1"],
        help="Prompt version; defaults to PROMPT_VERSION or v1.1",
    )
    parser.add_argument(
        "--provider",
        choices=["gemini", "mock"],
        help="Use gemini for evidence; mock is only an offline smoke test",
    )
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    settings = Settings()
    settings.validate()

    if not args.requirements.is_file():
        raise SystemExit(f"Requirements file not found: {args.requirements}")

    provider = args.provider or settings.provider
    prompt_version = args.prompt_version or settings.prompt_version
    requirements = args.requirements.read_text(encoding="utf-8")

    try:
        client = create_model_client(
            provider,
            settings.model_name,
            temperature=settings.temperature,
            max_output_tokens=settings.max_output_tokens,
        )
        result = TestPlanService(client).generate_plan(
            feature=args.feature,
            requirements=requirements,
            prompt_version=prompt_version,
        )
    except (RuntimeError, ValueError, ValidationError) as exc:
        print(f"CodeGuard baseline failed: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc

    output = {
        "model": result.model_name,
        "prompt_version": result.prompt_version,
        "latency_ms": result.latency_ms,
        "plan": result.plan.model_dump(),
    }
    rendered = json.dumps(output, indent=2)
    print(rendered)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
