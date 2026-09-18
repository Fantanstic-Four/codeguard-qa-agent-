from __future__ import annotations
import re
from .types import Chunk

def _tokens(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9_./-]+", text)

def chunk_document(
    *,
    source_id: str,
    title: str,
    path: str,
    text: str,
    chunk_size: int = 180,
    overlap: int = 35,
) -> list[Chunk]:
    """Create deterministic line-aware chunks without external dependencies."""
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")

    lines = text.splitlines()
    chunks: list[Chunk] = []
    start = 0
    number = 1

    while start < len(lines):
        end = start
        token_count = 0
        while end < len(lines):
            line_tokens = len(_tokens(lines[end]))
            if end > start and token_count + line_tokens > chunk_size:
                break
            token_count += line_tokens
            end += 1

        if end == start:
            end += 1

        body = "\n".join(lines[start:end]).strip()
        if body:
            chunks.append(
                Chunk(
                    chunk_id=f"{source_id}-C{number:03d}",
                    source_id=source_id,
                    title=title,
                    path=path,
                    text=body,
                    start_line=start + 1,
                    end_line=end,
                )
            )
            number += 1

        if end >= len(lines):
            break

        # Approximate overlap by walking backwards until enough tokens are retained.
        retained = 0
        next_start = end
        while next_start > start and retained < overlap:
            next_start -= 1
            retained += len(_tokens(lines[next_start]))
        start = max(next_start, start + 1)

    return chunks
