from packages.plugin_sdk.base import BasePlugin
from pathlib import Path
from datetime import datetime

class ImageGenPlugin(BasePlugin):
    name = "image_gen_plugin"
    version = "0.1.0"
    description = "Mock image generation plugin. Ready to be connected to ComfyUI."

    def run(self, payload):
        prompt = payload.get("prompt", "")
        output_dir = Path("/Users/mofamaomi/Documents/本地ai/generated/images")
        output_dir.mkdir(parents=True, exist_ok=True)

        fake_path = output_dir / f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        fake_path.write_text(
            f"MOCK IMAGE RESULT\nprompt={prompt}\nbackend=ComfyUI-placeholder\n",
            encoding="utf-8"
        )

        return {
            "ok": True,
            "plugin": self.name,
            "mode": "mock",
            "backend": "ComfyUI",
            "prompt": prompt,
            "output_path": str(fake_path)
        }
