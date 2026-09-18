# RAG Retrieval Policy
RAG-001: Week 3 uses a controlled, traceable corpus rather than relying only on model memory.
RAG-002: Corpus records are segmented into overlapping chunks before indexing.
RAG-003: Retrieval returns the highest-scoring relevant chunks up to the configured top-k limit.
RAG-004: Retrieved chunks expose source ID, chunk ID, file name, line range, and retrieval score.
RAG-005: The model context is constructed from retrieved evidence.
RAG-006: If retrieval produces no sufficiently relevant evidence, the system must not fabricate a grounded answer.
RAG-007: The initial Week 3 index is intentionally local and inspectable; it can later be replaced without changing the grounding contract.
