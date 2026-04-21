import requests
from packages.plugin_sdk.base import BasePlugin

class FinancePipelinePlugin(BasePlugin):
    name = "finance_pipeline_plugin"
    version = "0.2.0"
    description = "Finance realization pipeline shell"
    def run(self, payload):
        r = requests.post("http://127.0.0.1:18091/finance", json=payload, timeout=1200)
        r.raise_for_status()
        return r.json()
