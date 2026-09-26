# Week 3 File Manifest

This package is an **overlay for the existing Week 2 `codeguard-qa-agent` repository**.

## New Week 3 assets

- `knowledge/source-register.json`
- `knowledge/corpus/` — 12 controlled corpus records
- `src/codeguard/rag/` — ingestion, chunking, indexing, retrieval, grounding
- `src/codeguard/rag_cli.py` — retrieval inspection CLI
- `tests/test_rag_chunking.py`
- `tests/test_rag_index.py`
- `tests/test_rag_context.py`
- `evaluation/week3_rag_cases.json`
- `evaluation/run_week3_rag_eval.py`
- `evaluation/week3_rag_results.csv`
- `docs/rag/corpus-source-register.md`
- `docs/rag/retrieval-design.md`
- `docs/rag/failure-catalogue.md`
- `docs/architecture/rag-architecture.md`
- `docs/weekly-reports/week-03-task-allocation.md`
- `docs/weekly-reports/week-03.md`
- `WEEK3-RUN-GUIDE.md`

## Files intentionally not duplicated

The existing Week 2 `model_client.py`, `service.py`, `schema.py`, prompts, settings, and baseline tests should remain. Follow `WEEK3-RUN-GUIDE.md` to insert the RAG context immediately before the existing model invocation.
