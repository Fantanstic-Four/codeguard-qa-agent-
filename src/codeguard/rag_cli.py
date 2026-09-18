from __future__ import annotations
import argparse
import json
from .rag import RAGPipeline, TfidfIndex, load_corpus

def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect CodeGuard Week 3 retrieval.")
    parser.add_argument("query")
    parser.add_argument("--register", default="knowledge/source-register.json")
    parser.add_argument("--top-k", type=int, default=4)
    parser.add_argument("--min-score", type=float, default=0.08)
    args = parser.parse_args()

    chunks = load_corpus(args.register)
    pipeline = RAGPipeline(TfidfIndex(chunks), args.top_k, args.min_score)
    prompt, result = pipeline.augment_prompt(args.query)

    print(json.dumps({
        "query": args.query,
        "sources": result.source_citations,
        "retrieved": [
            {"citation": r.citation(), "score": round(r.score, 4), "text": r.chunk.text}
            for r in result.retrieved
        ],
        "augmented_prompt": prompt,
    }, indent=2))

if __name__ == "__main__":
    main()
