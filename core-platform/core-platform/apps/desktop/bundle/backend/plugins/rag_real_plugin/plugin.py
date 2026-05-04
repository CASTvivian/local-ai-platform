import requests
from packages.plugin_sdk.base import BasePlugin

class RAGRealPlugin(BasePlugin):
    name = "rag_real_plugin"
    version = "0.1.0"
    description = "RAG real integration shell plugin"
    def run(self, payload):
        r = requests.post("http://127.0.0.1:18091/rag", json=payload, timeout=1200)
        r.raise_for_status()
        return r.json()
