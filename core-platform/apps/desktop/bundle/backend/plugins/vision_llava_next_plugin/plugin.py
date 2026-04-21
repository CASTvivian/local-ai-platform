from packages.plugin_sdk.base import BasePlugin

class VisionLlavaNextPlugin(BasePlugin):
    name = "vision_llava_next_plugin"
    version = "0.1.0"
    description = "LLaVA-NeXT placeholder plugin"
    
    def run(self, payload):
        return {
            "ok": True, 
            "plugin": self.name, 
            "backend": "LLaVA-NeXT-placeholder", 
            "mode": "placeholder", 
            "query": payload.get("prompt", "")
        }
