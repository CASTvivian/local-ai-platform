from packages.plugin_sdk.base import BasePlugin

class VisionLlavaOV15Plugin(BasePlugin):
    name = "vision_llava_ov15_plugin"
    version = "0.1.0"
    description = "LLaVA-OneVision-1.5 placeholder plugin"
    
    def run(self, payload):
        return {
            "ok": True, 
            "plugin": self.name, 
            "backend": "LLaVA-OneVision-1.5-placeholder", 
            "mode": "placeholder", 
            "query": payload.get("prompt", "")
        }
