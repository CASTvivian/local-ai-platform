import requests
from packages.plugin_sdk.base import BasePlugin

class SkyvernPlugin(BasePlugin):
    name = "skyvern_plugin"
    version = "0.2.0"
    description = "skyvern standard action plugin"

    def run(self, payload):
        data = dict(payload)
        data["provider"] = "skyvern"
        data.setdefault("action", "form_flow")
        r = requests.post("http://127.0.0.1:18096/run", json=data, timeout=1800)
        r.raise_for_status()
        return r.json()
