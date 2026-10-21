import argparse
import json
from .pipeline import index_documents, search

parser = argparse.ArgumentParser()
parser.add_argument("--docs", required=True)
parser.add_argument("--query", required=True)
parser.add_argument("--access", choices=["public","internal"], default="public")
args = parser.parse_args()
print(json.dumps(search(index_documents(args.docs), args.query, args.access),indent=2))
