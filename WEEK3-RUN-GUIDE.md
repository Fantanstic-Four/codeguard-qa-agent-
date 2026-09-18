# CodeGuard Week 3 Run Guide

## 1. Copy these files into the existing Week 2 repository

Keep the existing Week 2 model client, schema, service, prompts, and CLI. Week 3 adds `src/codeguard/rag/`, a retrieval inspection CLI, a controlled corpus, tests, and evaluation assets.

## 2. Install the existing project

```bash
python -m pip install -e .
```

If the existing project has development dependencies:

```bash
python -m pip install -e ".[dev]"
```

## 3. Inspect retrieval before calling Gemini

```bash
python -m codeguard.rag_cli "What fields are required when creating an owner?"
```

Confirm that the output contains `CG-SRC-012` and a source/chunk citation.

## 4. Run RAG tests

```bash
pytest tests/test_rag_chunking.py tests/test_rag_index.py tests/test_rag_context.py -q
```

## 5. Run the 15-case retrieval evaluation

```bash
python evaluation/run_week3_rag_eval.py
```

This overwrites `evaluation/week3_rag_results.csv` with genuine retrieval results.

## 6. Connect retrieval to the existing Week 2 model call

Immediately before the existing Gemini invocation:

```python
from codeguard.rag import load_corpus, TfidfIndex, RAGPipeline

chunks = load_corpus("knowledge/source-register.json")
rag = RAGPipeline(TfidfIndex(chunks))
grounded_prompt, rag_result = rag.augment_prompt(user_task)

# Pass grounded_prompt into the same model-client path that Week 2 already uses.
# Preserve the existing schema validation.
# Record rag_result.source_citations in the trace/evidence.
```

Use the existing Week 2 model client rather than creating a second Gemini client.

## 7. Evidence to capture

Capture:
- successful RAG unit tests;
- one answerable retrieval trace;
- one partially answerable trace;
- one deliberately unanswerable trace;
- at least three genuine retrieval/grounding failures;
- the final 15-case results CSV;
- a screenshot or terminal output showing source citations.

Never fabricate pass/fail results. Replace all pending placeholders only after running the code.
