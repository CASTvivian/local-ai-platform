from packages.plugin_sdk.base import BasePlugin

class VisionQwen25VLPlugin(BasePlugin):
    name = "vision_qwen25vl_plugin"
    version = "0.1.0"
    description = "Qwen2.5-VL placeholder plugin"
    
    def run(self, payload):
        return {
            "ok": True, 
            "plugin": self.name, 
            "backend": "Qwen2.5-VL-placeholder", 
            "mode": "placeholder", 
            "query": payload.get("prompt", "")
        }
