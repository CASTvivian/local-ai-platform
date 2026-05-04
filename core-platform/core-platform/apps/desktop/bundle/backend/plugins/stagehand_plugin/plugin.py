import requests
from packages.plugin_sdk.base import BasePlugin

class StagehandPlugin(BasePlugin):
    name = "stagehand_plugin"
    version = "0.2.0"
    description = "stagehand standard action plugin"

    def run(self, payload):
        data = dict(payload)
        data["provider"] = "stagehand"
        data.setdefault("action", "extract")
        r = requests.post("http://127.0.0.1:18096/run", json=data, timeout=1800)
        r.raise_for_status()
        return r.json()
