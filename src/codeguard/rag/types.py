from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    source_id: str
    title: str
    path: str
    text: str
    start_line: int
    end_line: int

@dataclass(frozen=True)
class RetrievedChunk:
    chunk: Chunk
    score: float

    def citation(self) -> str:
        return (
            f"{self.chunk.source_id}::{self.chunk.chunk_id} "
            f"({Path(self.chunk.path).name}, lines "
            f"{self.chunk.start_line}-{self.chunk.end_line})"
        )
