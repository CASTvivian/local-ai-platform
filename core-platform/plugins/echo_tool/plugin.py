from packages.plugin_sdk.base import BasePlugin


class EchoToolPlugin(BasePlugin):
    name = "echo_tool"
    version = "0.1.0"
    description = "Echo back the payload for plugin-manager testing."

    def run(self, payload):
        return {
            "ok": True,
            "plugin": self.name,
            "version": self.version,
            "received": payload,
        }
