# Week 3 RAG Architecture

```mermaid
flowchart LR
    A[Controlled corpus\n10–50 approved records] --> B[Ingestion\nsource register + file loader]
    B --> C[Chunking\n~180 tokens, ~35 overlap]
    C --> D[TF-IDF index]
    Q[User task / feature question] --> E[Retriever\ntop-k=4, threshold=0.08]
    D --> E
    E --> F[Retrieved chunks\nsource ID + chunk ID + score]
    F --> G[Context builder]
    G --> H[Grounded prompt\nretrieved evidence + task]
    H --> I[Existing Gemini model client\nGemini 3.1 Flash-Lite]
    I --> J[Schema-validated response]
    F --> K[Retrieval trace / visible sources]
    J --> L[Reviewable test-plan response]
```

## Data flow

1. `knowledge/source-register.json` records provenance and the approved corpus paths.
2. `load_corpus()` reads Markdown/text records and creates line-aware overlapping chunks.
3. `TfidfIndex` builds a local, deterministic lexical index suitable for the small controlled corpus.
4. `RAGPipeline.retrieve()` ranks chunks using cosine similarity and keeps up to four above the minimum threshold.
5. `build_grounded_context()` exposes source ID, chunk ID, file, line range, score, and evidence text.
6. The augmented prompt instructs the existing Week 2 model layer to use only retrieved evidence for project-specific factual claims.
7. When evidence is absent or incomplete, the expected behavior is clarification rather than invention.

## Boundary

Week 3 adds retrieval and grounding only. Repository inspection, arbitrary shell execution, autonomous merge/deployment, memory, and unrestricted tools remain outside this week's scope.
