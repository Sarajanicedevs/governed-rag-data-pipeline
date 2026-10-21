from pathlib import Path
from governed_retrieval.pipeline import index_documents, search

def test_public_access(tmp_path: Path):
    (tmp_path/"open.md").write_text("access: public\nquality data contracts")
    (tmp_path/"secret.md").write_text("access: internal\nquality restricted contracts")
    docs = index_documents(tmp_path)
    assert [r["source"] for r in search(docs, "quality contracts", access="public")] == ["open.md"]
    assert len(search(docs,"quality contracts",access="internal")) == 2

def test_unknown_access_denied():
    try:
        search([], "hello", access="admin")
    except ValueError:
        return
    assert False
