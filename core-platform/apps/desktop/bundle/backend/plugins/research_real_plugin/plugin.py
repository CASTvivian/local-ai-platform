import requests
from packages.plugin_sdk.base import BasePlugin

class ResearchRealPlugin(BasePlugin):
    name = "research_real_plugin"
    version = "1.2.0"
    description = "Structured lightweight research realization plugin"

    def run(self, payload):
        action = payload.get("action", "search")
        if action == "news_summary":
            url = "http://127.0.0.1:18098/news_summary"
        elif action == "stock_report":
            url = "http://127.0.0.1:18098/stock_report"
        else:
            url = "http://127.0.0.1:18098/search"

        r = requests.post(url, json=payload, timeout=1800)
        r.raise_for_status()
        return r.json()
