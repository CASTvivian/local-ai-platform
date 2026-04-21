import requests
from packages.plugin_sdk.base import BasePlugin

class HyperframesPlugin(BasePlugin):
    name = "hyperframes_plugin"
    version = "1.2.0"
    description = "HyperFrames video template/render plugin"

    def run(self, payload):
        action = payload.get("action", "probe")
        if action == "render":
            url = "http://127.0.0.1:18099/render"
            r = requests.post(url, json=payload, timeout=1800)
        elif action == "research_to_video":
            url = "http://127.0.0.1:18099/research_to_video"
            r = requests.post(url, json=payload, timeout=1800)
        else:
            url = "http://127.0.0.1:18099/probe"
            r = requests.get(url, timeout=1800)
        r.raise_for_status()
        return r.json()
