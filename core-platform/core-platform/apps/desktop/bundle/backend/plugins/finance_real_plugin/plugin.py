import requests
from packages.plugin_sdk.base import BasePlugin

class FinanceRealPlugin(BasePlugin):
    name = "finance_real_plugin"
    version = "0.1.0"
    description = "Finance real integration shell plugin"
    def run(self, payload):
        r = requests.post("http://127.0.0.1:18091/finance", json=payload, timeout=1200)
        r.raise_for_status()
        return r.json()
