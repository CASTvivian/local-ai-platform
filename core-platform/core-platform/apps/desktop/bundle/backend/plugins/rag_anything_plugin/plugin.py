from packages.plugin_sdk.base import BasePlugin

class RAGAnythingPlugin(BasePlugin):
    name = "rag_anything_plugin"
    version = "0.1.0"
    description = "RAG-Anything placeholder plugin"
    
    def run(self, payload):
        return {
            "ok": True, 
            "plugin": self.name, 
            "backend": "RAG-Anything-placeholder", 
            "mode": "placeholder", 
            "query": payload.get("prompt", "")
        }
