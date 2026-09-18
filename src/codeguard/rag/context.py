from __future__ import annotations
from .types import RetrievedChunk

def build_grounded_context(results: list[RetrievedChunk]) -> str:
    if not results:
        return "NO_RETRIEVED_EVIDENCE"

    sections = []
    for result in results:
        sections.append(
            f"[SOURCE {result.citation()} | score={result.score:.3f}]\n"
            f"{result.chunk.text}"
        )
    return "\n\n".join(sections)

def grounding_instructions() -> str:
    return """Use only the RETRIEVED EVIDENCE below for factual claims about the project.
Cite source IDs/chunk IDs for every material claim.
If the evidence is incomplete, explicitly say what is missing.
If no evidence supports the request, return status=clarification_required and do not invent details.
Do not claim that code/tests passed unless execution evidence is present."""
