import json
import random
import time
from pathlib import Path

import requests

from packages.plugin_sdk.base import BasePlugin

class ImageGenPlugin(BasePlugin):
    name = "image_gen_plugin"
    version = "0.2.0"
    description = "Image generation plugin backed by ComfyUI."

    def run(self, payload):
        prompt = payload.get("prompt", "").strip()
        negative_prompt = payload.get("negative_prompt", "bad hands, blurry, low quality")
        width = int(payload.get("width", 512))
        height = int(payload.get("height", 512))
        steps = int(payload.get("steps", 20))
        seed = int(payload.get("seed", random.randint(1, 999999999)))

        comfy_base = "http://127.0.0.1:8188"
        workflow_path = Path("/Users/mofamaomi/Documents/本地ai/core-platform/manifests/workflows/comfyui_basic_t2i.json")

        # Try real ComfyUI connection
        try:
            if not workflow_path.exists():
                raise FileNotFoundError(f"workflow not found: {workflow_path}")

            workflow = json.loads(workflow_path.read_text(encoding="utf-8"))

            workflow["6"]["inputs"]["text"] = prompt or "masterpiece best quality landscape"
            workflow["7"]["inputs"]["text"] = negative_prompt
            workflow["3"]["inputs"]["seed"] = seed
            workflow["3"]["inputs"]["steps"] = steps
            workflow["5"]["inputs"]["width"] = width
            workflow["5"]["inputs"]["height"] = height

            # queue prompt
            queue_resp = requests.post(
                f"{comfy_base}/prompt",
                json={"prompt": workflow},
                timeout=60
            )
            queue_resp.raise_for_status()
            queue_data = queue_resp.json()

            prompt_id = queue_data.get("prompt_id")
            if not prompt_id:
                raise ValueError("ComfyUI did not return prompt_id")

            # poll history
            history_data = None
            for _ in range(120):
                time.sleep(1.5)
                history_resp = requests.get(f"{comfy_base}/history/{prompt_id}", timeout=30)
                history_resp.raise_for_status()
                history_json = history_resp.json()
                if prompt_id in history_json:
                    history_data = history_json[prompt_id]
                    break

            if not history_data:
                raise TimeoutError("ComfyUI generation timeout")

            output_images = []
            outputs = history_data.get("outputs", {})

            for node_id, node_output in outputs.items():
                if "images" in node_output:
                    for image in node_output["images"]:
                        filename = image.get("filename")
                        subfolder = image.get("subfolder", "")
                        folder_type = image.get("type", "output")
                        output_url = f"{comfy_base}/view?filename={filename}&subfolder={subfolder}&type={folder_type}"

                        output_images.append({
                            "node_id": node_id,
                            "filename": filename,
                            "subfolder": subfolder,
                            "type": folder_type,
                            "output_url": output_url
                        })

            if not output_images:
                raise ValueError("No images found in ComfyUI history output")

            first = output_images[0]

            return {
                "ok": True,
                "plugin": self.name,
                "backend": "ComfyUI",
                "mode": "real",
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "seed": seed,
                "width": width,
                "height": height,
                "steps": steps,
                "prompt_id": prompt_id,
                "images": output_images,
                "output_url": first["output_url"],
                "filename": first["filename"]
            }

        except Exception as e:
            # Fallback to mock mode
            output_dir = Path("/Users/mofamaomi/Documents/本地ai/generated/images")
            output_dir.mkdir(parents=True, exist_ok=True)

            fake_path = output_dir / f"image_{time.strftime('%Y%m%d_%H%M%S')}.txt"
            fake_path.write_text(
                f"MOCK IMAGE RESULT (ComfyUI unavailable)\n"
                f"prompt={prompt}\n"
                f"backend=ComfyUI\n"
                f"error={str(e)}\n"
                f"seed={seed}\n"
                f"width={width}x{height}\n"
                f"steps={steps}",
                encoding="utf-8"
            )

            return {
                "ok": True,
                "plugin": self.name,
                "backend": "ComfyUI",
                "mode": "mock",
                "prompt": prompt,
                "error": str(e),
                "output_path": str(fake_path),
                "note": "ComfyUI unavailable, using mock mode. Download models to enable real generation."
            }
