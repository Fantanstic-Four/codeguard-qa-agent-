from codeguard.rag.context import build_grounded_context
from codeguard.rag.types import Chunk, RetrievedChunk

def test_context_exposes_source_and_score():
    chunk = Chunk("SRC-C001","SRC","Title","doc.md","Evidence text",3,5)
    context = build_grounded_context([RetrievedChunk(chunk, 0.42)])
    assert "SRC::SRC-C001" in context
    assert "lines 3-5" in context
    assert "score=0.420" in context
    assert "Evidence text" in context
