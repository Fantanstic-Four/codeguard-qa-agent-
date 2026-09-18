from __future__ import annotations
import json
from pathlib import Path
from .chunking import chunk_document
from .types import Chunk

SUPPORTED = {".md", ".txt"}

def load_source_register(register_path: str | Path) -> list[dict]:
    data = json.loads(Path(register_path).read_text(encoding="utf-8"))
    sources = data.get("sources", [])
    if not sources:
        raise ValueError("Source register contains no sources.")
    return sources

def load_corpus(
    register_path: str | Path,
    *,
    chunk_size: int = 180,
    overlap: int = 35,
) -> list[Chunk]:
    register_path = Path(register_path)
    repo_root = register_path.parents[1]
    chunks: list[Chunk] = []

    for source in load_source_register(register_path):
        source_path = repo_root / source["path"]
        if source_path.suffix.lower() not in SUPPORTED:
            raise ValueError(f"Unsupported corpus file: {source_path}")
        if not source_path.exists():
            raise FileNotFoundError(source_path)

        text = source_path.read_text(encoding="utf-8")
        chunks.extend(
            chunk_document(
                source_id=source["source_id"],
                title=source["title"],
                path=source["path"],
                text=text,
                chunk_size=chunk_size,
                overlap=overlap,
            )
        )
    return chunks
