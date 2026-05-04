import requests
from packages.plugin_sdk.base import BasePlugin

class VisionRealPlugin(BasePlugin):
    name = "vision_real_plugin"
    version = "0.1.0"
    description = "Vision real integration shell plugin"
    def run(self, payload):
        r = requests.post("http://127.0.0.1:18091/vision", json=payload, timeout=1200)
        r.raise_for_status()
        return r.json()
