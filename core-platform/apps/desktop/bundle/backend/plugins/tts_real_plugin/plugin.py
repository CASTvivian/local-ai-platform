import requests
from packages.plugin_sdk.base import BasePlugin

class TTSRealPlugin(BasePlugin):
    name = "tts_real_plugin"
    version = "0.1.0"
    description = "TTS real integration shell plugin"
    def run(self, payload):
        r = requests.post("http://127.0.0.1:18091/tts", json=payload, timeout=1200)
        r.raise_for_status()
        return r.json()
