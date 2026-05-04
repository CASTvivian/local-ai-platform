import requests
from packages.plugin_sdk.base import BasePlugin

class BrowserUsePlugin(BasePlugin):
    name = "browser_use_plugin"
    version = "0.2.0"
    description = "browser-use standard action plugin"

    def run(self, payload):
        data = dict(payload)
        data["provider"] = "browser_use"
        data.setdefault("action", "navigate")
        r = requests.post("http://127.0.0.1:18096/run", json=data, timeout=1800)
        r.raise_for_status()
        return r.json()
