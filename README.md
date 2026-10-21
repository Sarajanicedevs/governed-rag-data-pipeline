# Governed Retrieval Data Pipeline

A compact, reproducible retrieval pipeline emphasizing metadata, provenance and access filters. Synthetic documents are indexed locally and retrieved using token-overlap scoring, without a paid API or production data.

## Quick start
```bash
python -m pip install -e '.[dev]'
python -m governed_retrieval --docs data/docs --query "data contracts" --access public
pytest -q
```

It demonstrates **data preparation for RAG**; it is not a full LLM deployment or vector database. A production version would add a vetted embeddings model, identity-backed authorization, encryption, privacy review and labeled relevance evaluations.
