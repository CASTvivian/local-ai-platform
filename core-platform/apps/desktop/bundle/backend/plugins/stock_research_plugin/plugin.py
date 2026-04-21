import requests
from packages.plugin_sdk.base import BasePlugin

class StockResearchPlugin(BasePlugin):
    name = "stock_research_plugin"
    version = "0.1.0"
    description = "Stock research realtime shell"
    def run(self, payload):
        r = requests.post("http://127.0.0.1:18092/stock_research", json=payload, timeout=1200)
        r.raise_for_status()
        return r.json()
