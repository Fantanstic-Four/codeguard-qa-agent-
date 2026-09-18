from __future__ import annotations
import math
import re
from collections import Counter, defaultdict
from .types import Chunk, RetrievedChunk

TOKEN_RE = re.compile(r"[a-z0-9_./-]+")

def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())

class TfidfIndex:
    """Small, inspectable TF-IDF retrieval index suitable for the controlled Week 3 corpus."""

    def __init__(self, chunks: list[Chunk]):
        if not chunks:
            raise ValueError("Cannot index an empty corpus.")
        self.chunks = chunks
        self.doc_tf = [Counter(tokenize(c.text)) for c in chunks]
        df = defaultdict(int)
        for tf in self.doc_tf:
            for term in tf:
                df[term] += 1
        n = len(chunks)
        self.idf = {term: math.log((n + 1) / (freq + 1)) + 1 for term, freq in df.items()}
        self.doc_vectors = [self._vector(tf) for tf in self.doc_tf]

    def _vector(self, tf: Counter) -> dict[str, float]:
        return {term: (1 + math.log(freq)) * self.idf.get(term, 0.0) for term, freq in tf.items()}

    @staticmethod
    def _cosine(a: dict[str, float], b: dict[str, float]) -> float:
        common = set(a) & set(b)
        dot = sum(a[t] * b[t] for t in common)
        na = math.sqrt(sum(v * v for v in a.values()))
        nb = math.sqrt(sum(v * v for v in b.values()))
        return dot / (na * nb) if na and nb else 0.0

    def search(self, query: str, top_k: int = 4, min_score: float = 0.08) -> list[RetrievedChunk]:
        qtf = Counter(tokenize(query))
        qv = self._vector(qtf)
        scored = [
            RetrievedChunk(chunk=chunk, score=self._cosine(qv, dv))
            for chunk, dv in zip(self.chunks, self.doc_vectors)
        ]
        return [r for r in sorted(scored, key=lambda x: x.score, reverse=True)
                if r.score >= min_score][:top_k]
