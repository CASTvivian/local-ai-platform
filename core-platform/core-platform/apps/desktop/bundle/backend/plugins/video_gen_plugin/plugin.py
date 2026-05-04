from packages.plugin_sdk.base import BasePlugin
from pathlib import Path
from datetime import datetime

class VideoGenPlugin(BasePlugin):
    name = "video_gen_plugin"
    version = "0.1.0"
    description = "Mock video generation plugin. Ready to be connected to CogVideo."

    def run(self, payload):
        prompt = payload.get("prompt", "")
        output_dir = Path("/Users/mofamaomi/Documents/本地ai/generated/videos")
        output_dir.mkdir(parents=True, exist_ok=True)

        fake_path = output_dir / f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        fake_path.write_text(
            f"MOCK VIDEO RESULT\nprompt={prompt}\nbackend=CogVideo-placeholder\n",
            encoding="utf-8"
        )

        return {
            "ok": True,
            "plugin": self.name,
            "mode": "mock",
            "backend": "CogVideo",
            "prompt": prompt,
            "output_path": str(fake_path)
        }
