import requests
from packages.plugin_sdk.base import BasePlugin

class RAGPipelinePlugin(BasePlugin):
    name = "rag_pipeline_plugin"
    version = "0.2.0"
    description = "RAG realization pipeline shell"
    def run(self, payload):
        r = requests.post("http://127.0.0.1:18091/rag", json=payload, timeout=1200)
        r.raise_for_status()
        return r.json()
