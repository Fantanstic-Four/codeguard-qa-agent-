# Week 3 Task Allocation — Four Members

| Member | Primary ownership | Files | Difficulty |
|---|---|---|---|
| Member 1 | Corpus, provenance and ingestion | `knowledge/corpus/*`, `knowledge/source-register.json`, `docs/rag/corpus-source-register.md`, `src/codeguard/rag/chunking.py`, `src/codeguard/rag/ingest.py`, `tests/test_rag_chunking.py` | Medium (3/5) |
| Member 2 | Retrieval/indexing implementation | `src/codeguard/rag/types.py`, `index.py`, `pipeline.py`, `rag_cli.py`, `tests/test_rag_index.py`, `docs/rag/retrieval-design.md` | Hard (4/5) |
| Member 3 | Grounding, architecture and model integration | `src/codeguard/rag/context.py`, `src/codeguard/rag/__init__.py`, `tests/test_rag_context.py`, `docs/architecture/rag-architecture.md`, Week 2 service/model integration, source trace evidence | Hard (4/5) |
| Member 4 | Evaluation, failures and weekly evidence | `evaluation/week3_rag_cases.json`, `run_week3_rag_eval.py`, `week3_rag_results.csv`, `docs/rag/failure-catalogue.md`, `WEEK3-RUN-GUIDE.md`, `docs/weekly-reports/week-03.md` | Medium–Hard (3.5/5) |

All members should review the complete RAG flow and be able to explain ingestion → chunking → indexing → retrieval → grounded context → model response.
