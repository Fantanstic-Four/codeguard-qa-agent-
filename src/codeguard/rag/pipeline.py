from __future__ import annotations
from dataclasses import dataclass
from .context import build_grounded_context, grounding_instructions
from .index import TfidfIndex
from .types import RetrievedChunk

@dataclass
class RAGResult:
    query: str
    retrieved: list[RetrievedChunk]
    context: str

    @property
    def source_citations(self) -> list[str]:
        return [item.citation() for item in self.retrieved]

class RAGPipeline:
    def __init__(self, index: TfidfIndex, top_k: int = 4, min_score: float = 0.08):
        self.index = index
        self.top_k = top_k
        self.min_score = min_score

    def retrieve(self, query: str) -> RAGResult:
        results = self.index.search(query, top_k=self.top_k, min_score=self.min_score)
        return RAGResult(
            query=query,
            retrieved=results,
            context=build_grounded_context(results),
        )

    def augment_prompt(self, query: str) -> tuple[str, RAGResult]:
        result = self.retrieve(query)
        prompt = (
            grounding_instructions()
            + "\n\nRETRIEVED EVIDENCE:\n"
            + result.context
            + "\n\nUSER TASK:\n"
            + query
        )
        return prompt, result
