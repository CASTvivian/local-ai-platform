from packages.plugin_sdk.base import BasePlugin

class VisionQwen3VLPlugin(BasePlugin):
    name = "vision_qwen3vl_plugin"
    version = "0.1.0"
    description = "Qwen3-VL placeholder plugin"
    
    def run(self, payload):
        return {
            "ok": True, 
            "plugin": self.name, 
            "backend": "Qwen3-VL-placeholder", 
            "mode": "placeholder", 
            "query": payload.get("prompt", "")
        }
