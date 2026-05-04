from packages.plugin_sdk.base import BasePlugin

class FinanceQlibPlugin(BasePlugin):
    name = "finance_qlib_plugin"
    version = "0.1.0"
    description = "Qlib placeholder plugin"
    
    def run(self, payload):
        return {
            "ok": True, 
            "plugin": self.name, 
            "backend": "Qlib-placeholder", 
            "mode": "placeholder", 
            "query": payload.get("prompt", "")
        }
