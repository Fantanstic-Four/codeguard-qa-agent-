from codeguard.rag.chunking import chunk_document

def test_chunking_keeps_traceable_line_ranges():
    text = "\n".join(f"REQ-{i}: requirement number {i}" for i in range(1, 30))
    chunks = chunk_document(
        source_id="TEST-SRC", title="Test", path="test.md",
        text=text, chunk_size=25, overlap=5
    )
    assert len(chunks) > 1
    assert chunks[0].source_id == "TEST-SRC"
    assert chunks[0].start_line == 1
    assert all(c.start_line <= c.end_line for c in chunks)
