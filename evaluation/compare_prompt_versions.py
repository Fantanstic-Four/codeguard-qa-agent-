"""Compare genuine Week 2 CSV results and write a Markdown summary."""

from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parent


def read_results(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise SystemExit(f"Missing results file: {path}")
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 10:
        raise SystemExit(f"Expected 10 cases in {path}, found {len(rows)}")
    return rows


def summarize(rows: list[dict[str, str]]) -> dict[str, float | int]:
    latencies = [float(row["latency_ms"]) for row in rows if row["latency_ms"]]
    return {
        "cases": len(rows),
        "schema": sum(row["schema_valid"] == "yes" for row in rows),
        "grounding": sum(row["grounding_ok"] == "yes" for row in rows),
        "coverage": sum(row["coverage_ok"] == "yes" for row in rows),
        "passed": sum(row["result"] == "PASS" for row in rows),
        "mean_latency": round(mean(latencies)) if latencies else 0,
    }


def main() -> None:
    summaries = {
        "v1.0": summarize(read_results(ROOT / "results-v1.0.csv")),
        "v1.1": summarize(read_results(ROOT / "results-v1.1.csv")),
    }
    lines = [
        "# Week 2 Prompt Comparison",
        "",
        "| Metric | v1.0 | v1.1 |",
        "|---|---:|---:|",
        f"| Cases executed | {summaries['v1.0']['cases']} | {summaries['v1.1']['cases']} |",
        f"| Schema-valid responses | {summaries['v1.0']['schema']} | {summaries['v1.1']['schema']} |",
        f"| Grounding checks passed | {summaries['v1.0']['grounding']} | {summaries['v1.1']['grounding']} |",
        f"| Coverage checks passed | {summaries['v1.0']['coverage']} | {summaries['v1.1']['coverage']} |",
        f"| Overall cases passed | {summaries['v1.0']['passed']} | {summaries['v1.1']['passed']} |",
        f"| Mean latency in milliseconds | {summaries['v1.0']['mean_latency']} | {summaries['v1.1']['mean_latency']} |",
        "",
        "Selected prompt: TEAM TO COMPLETE AFTER REVIEW",
        "",
        "Evidence-based reason: TEAM TO COMPLETE AFTER INSPECTING FAILED CASES",
    ]
    output = ROOT / "week2_prompt_comparison.md"
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()