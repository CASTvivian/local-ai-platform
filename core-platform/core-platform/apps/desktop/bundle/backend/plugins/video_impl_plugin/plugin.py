import requests
from packages.plugin_sdk.base import BasePlugin

class VideoImplPlugin(BasePlugin):
    name = "video_impl_plugin"
    version = "1.0.0"
    description = "Real CogVideo implementation plugin"

    def run(self, payload):
        r = requests.post(
            "http://127.0.0.1:18097/video/generate",
            json=payload,
            timeout=3600
        )
        r.raise_for_status()
        return r.json()
