from packages.plugin_sdk.base import BasePlugin

class FinanceVnpyPlugin(BasePlugin):
    name = "finance_vnpy_plugin"
    version = "0.1.0"
    description = "vn.py finance plugin placeholder."

    def run(self, payload):
        prompt = payload.get("prompt", "").strip()
        return {
            "ok": True,
            "plugin": self.name,
            "backend": "vn.py-placeholder",
            "mode": "placeholder",
            "result": {
                "summary": "vn.py integration placeholder ready",
                "query": prompt,
                "next_step": "connect strategy/backtest/execution modules later"
            }
        }
