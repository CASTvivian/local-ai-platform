import requests
from packages.plugin_sdk.base import BasePlugin

class RAGImplPlugin(BasePlugin):
    name = "rag_impl_plugin"
    version = "1.1.0"
    description = "Real RAG implementation plugin"

    def run(self, payload):
        action = payload.get("action", "query")
        if action == "index":
            r = requests.post("http://127.0.0.1:18095/rag/index", json=payload, timeout=1800)
        else:
            r = requests.post("http://127.0.0.1:18095/rag/query", json=payload, timeout=1800)
        r.raise_for_status()
        return r.json()
