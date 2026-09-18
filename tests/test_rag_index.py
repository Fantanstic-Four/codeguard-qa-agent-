from codeguard.rag.index import TfidfIndex
from codeguard.rag.types import Chunk

def test_retriever_ranks_relevant_chunk_first():
    chunks = [
        Chunk("A-C001","A","Owner Search","a.md","Search owners by last name",1,1),
        Chunk("B-C001","B","Deployment","b.md","Production deployment is prohibited",1,1),
    ]
    results = TfidfIndex(chunks).search("owner last name search", top_k=2, min_score=0.0)
    assert results[0].chunk.source_id == "A"

def test_high_threshold_can_return_no_evidence():
    chunks = [Chunk("A-C001","A","Owners","a.md","Search owners by last name",1,1)]
    results = TfidfIndex(chunks).search("quantum satellite telemetry", min_score=0.9)
    assert results == []
