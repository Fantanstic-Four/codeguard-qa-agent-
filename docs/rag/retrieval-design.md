# Retrieval Design Note

## Why this design

The Week 3 corpus is deliberately small and controlled. The reference implementation therefore uses an inspectable TF-IDF index instead of introducing a hosted vector database. This keeps ingestion, indexing, ranking, source tracing, and failure analysis visible to the team.

## Segmentation

Documents are chunked to a target of about 180 lexical tokens with about 35 tokens of overlap. Original line ranges are retained for traceability.

## Retrieval

Queries and chunks are represented as TF-IDF vectors and ranked using cosine similarity. Defaults are `top_k=4` and `min_score=0.08`.

## Grounding

Retrieved chunks are inserted into a delimited `RETRIEVED EVIDENCE` section. The grounding contract requires source/chunk citations, distinguishes partial support from full support, and requires clarification when evidence is absent.

## Known limitation

Lexical retrieval can miss semantically related wording that shares few terms with the corpus. This is intentionally documented as a Week 3 failure mode and provides a clear future comparison point for embedding-based retrieval.
