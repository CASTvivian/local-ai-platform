import requests
from packages.plugin_sdk.base import BasePlugin

class FinanceImplPlugin(BasePlugin):
    name = "finance_impl_plugin"
    version = "1.1.0"
    description = "Real finance implementation plugin"

    def run(self, payload):
        r = requests.post("http://127.0.0.1:18095/finance/research", json=payload, timeout=1800)
        r.raise_for_status()
        return r.json()
