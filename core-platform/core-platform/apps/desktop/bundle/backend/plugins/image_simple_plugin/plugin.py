from packages.plugin_sdk.base import BasePlugin

class ImageSimplePlugin(BasePlugin):
    name = "image_simple_plugin"
    version = "0.1.0"
    description = "Fooocus/simple image mode placeholder."

    def run(self, payload):
        prompt = payload.get("prompt", "").strip()
        return {
            "ok": True,
            "plugin": self.name,
            "backend": "Fooocus-placeholder",
            "mode": "placeholder",
            "prompt": prompt,
            "note": "simple image mode placeholder integrated; connect real Fooocus backend later"
        }
