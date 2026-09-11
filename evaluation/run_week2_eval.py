"""Run the ten-case Week 2 prompt evaluation and write an evidence CSV."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

from codeguard.model_client import create_model_client
from codeguard.service import TestPlanService
from codeguard.settings import Settings


EXECUTION_CLAIM = re.compile(r"\b(passed|failed|executed successfully|we ran)\b", re.I)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt-version", choices=["v1.0", "v1.1"], required=True)
    parser.add_argument("--provider", choices=["gemini", "mock"], default="gemini")
    parser.add_argument(
        "--cases",
        type=Path,
        default=Path(__file__).with_name("week2_cases.json"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Defaults to evaluation/results-<prompt-version>.csv",
    )
    return parser


def score_case(case: dict, plan: dict) -> tuple[bool, bool, bool, str]:
    status_match = plan["status"] == case["expected_status"]
    tests = plan.get("tests", [])
    actual_refs = {
        ref for test in tests for ref in test.get("requirement_refs", [])
    }
    grounding_ok = set(case["required_refs"]).issubset(actual_refs)
    if case["expected_status"] == "needs_clarification":
        grounding_ok = grounding_ok and not tests

    actual_types = {test.get("test_type") for test in tests}
    coverage_ok = set(case["required_test_types"]).issubset(actual_types)
    rendered = json.dumps(plan)
    no_execution_claim = not EXECUTION_CLAIM.search(rendered)
    passed = status_match and grounding_ok and coverage_ok and no_execution_claim
    notes = (
        f"status={status_match}; grounding={grounding_ok}; "
        f"types={coverage_ok}; no_execution_claim={no_execution_claim}"
    )
    return passed, grounding_ok, coverage_ok, notes


def main() -> None:
    args = build_parser().parse_args()
    settings = Settings()
    output = args.output or Path(__file__).with_name(
        f"results-{args.prompt_version}.csv"
    )
    cases = json.loads(args.cases.read_text(encoding="utf-8"))
    settings.validate()
    client = create_model_client(
        args.provider,
        settings.model_name,
        temperature=settings.temperature,
        max_output_tokens=settings.max_output_tokens,
    )
    service = TestPlanService(client)
    rows = []

    for case in cases:
        try:
            result = service.generate_plan(
                feature=case["feature"],
                requirements=case["requirements"],
                prompt_version=args.prompt_version,
            )
            plan = result.plan.model_dump()
            passed, grounding_ok, coverage_ok, notes = score_case(case, plan)
            rows.append(
                {
                    "case_id": case["case_id"],
                    "category": case["category"],
                    "expected": case["expected_behavior"],
                    "prompt_version": args.prompt_version,
                    "model": client.model_name,
                    "actual_status": plan["status"],
                    "schema_valid": "yes",
                    "grounding_ok": "yes" if grounding_ok else "no",
                    "coverage_ok": "yes" if coverage_ok else "no",
                    "latency_ms": result.latency_ms,
                    "result": "PASS" if passed else "FAIL",
                    "notes": notes,
                }
            )
        except Exception as exc:  # evidence runner records the failure and continues
            rows.append(
                {
                    "case_id": case["case_id"],
                    "category": case["category"],
                    "expected": case["expected_behavior"],
                    "prompt_version": args.prompt_version,
                    "model": client.model_name,
                    "actual_status": "error",
                    "schema_valid": "no",
                    "grounding_ok": "no",
                    "coverage_ok": "no",
                    "latency_ms": "",
                    "result": "FAIL",
                    "notes": f"{type(exc).__name__}: {exc}",
                }
            )

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    passed = sum(row["result"] == "PASS" for row in rows)
    print(f"model={client.model_name}")
    print(f"prompt={args.prompt_version}")
    print(f"cases={len(rows)} passed={passed} failed={len(rows) - passed}")
    print(f"results={output}")
    if args.provider == "mock":
        print("WARNING: mock results are smoke-test output, not foundation-model evidence.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Evaluation interrupted.", file=sys.stderr)
        raise SystemExit(130)