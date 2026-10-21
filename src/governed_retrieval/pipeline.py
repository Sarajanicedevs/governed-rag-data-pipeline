"""Local retrieval with source provenance and document access labels."""
import hashlib
import re
from pathlib import Path

def tokens(value):
    return set(re.findall(r"[a-z0-9]+", value.lower()))

def index_documents(directory):
    records = []
    for path in sorted(Path(directory).glob("*.md")):
        content = path.read_text(encoding="utf-8")
        lines = content.splitlines()
        access = "public"
        if lines and lines[0].startswith("access:"):
            access = lines[0].split(":", 1)[1].strip().lower()
            content = "\n".join(lines[1:])
        if access not in {"public","internal"}:
            continue
        records.append({
          "source": path.name,
          "access": access,
          "version": hashlib.sha256(content.encode()).hexdigest()[:12],
          "content": content
        })
    return records

def search(records, query, access="public", limit=3):
    if access not in {"public","internal"}:
        raise ValueError("Invalid access level")
    q = tokens(query)
    allowed = {"public"} if access == "public" else {"public","internal"}
    matches = []
    for record in records:
        if record["access"] not in allowed:
            continue
        score = len(q & tokens(record["content"]))
        if score:
            matches.append({**record, "score":score})
    return sorted(matches,key=lambda r:(-r["score"],r["source"]))[:limit]
