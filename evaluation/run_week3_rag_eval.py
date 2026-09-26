from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
from codeguard.rag import RAGPipeline, TfidfIndex, load_corpus

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", default="evaluation/week3_rag_cases.json")
    parser.add_argument("--register", default="knowledge/source-register.json")
    parser.add_argument("--output", default="evaluation/week3_rag_results.csv")
    args = parser.parse_args()

    cases = json.loads(Path(args.cases).read_text(encoding="utf-8"))["cases"]
    chunks = load_corpus(args.register)
    pipeline = RAGPipeline(TfidfIndex(chunks))

    rows = []
    for case in cases:
        result = pipeline.retrieve(case["question"])
        actual_sources = sorted({r.chunk.source_id for r in result.retrieved})
        expected = case["expected_source_ids"]
        source_hit = (not expected and not actual_sources) or bool(set(expected) & set(actual_sources))
        rows.append({
            "case_id": case["case_id"],
            "category": case["category"],
            "question": case["question"],
            "expected_sources": ";".join(expected),
            "retrieved_sources": ";".join(actual_sources),
            "top_score": f"{result.retrieved[0].score:.4f}" if result.retrieved else "",
            "source_hit": str(source_hit).lower(),
            "grounding_result": "PENDING_MODEL_RUN",
            "notes": "",
        })

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} retrieval results to {out}")

if __name__ == "__main__":
    main()
