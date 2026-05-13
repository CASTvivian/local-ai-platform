# Missing Repo Summary Source: lllyasviel/Fooocus

- URL: https://github.com/lllyasviel/Fooocus
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/lllyasviel__Fooocus
- Clone Status: cloned
- Language: Python
- Stars: 48466
- Topics: 
- Description: Focus on prompting and generating

## Extracted README / Docs / Examples



# FILE: readme.md

<div align=center>
<img src="https://github.com/lllyasviel/Fooocus/assets/19834515/483fb86d-c9a2-4c20-997c-46dafc124f25">
</div>

# Fooocus

[>>> Click Here to Install Fooocus <<<](#download)

Fooocus is an image generating software (based on [Gradio](https://www.gradio.app/) <a href='https://github.com/gradio-app/gradio'><img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>).

Fooocus presents a rethinking of image generator designs. The software is offline, open source, and free, while at the same time, similar to many online image generators like Midjourney, the manual tweaking is not needed, and users only need to focus on the prompts and images. Fooocus has also simplified the installation: between pressing "download" and generating the first image, the number of needed mouse clicks is strictly limited to less than 3. Minimal GPU memory requirement is 4GB (Nvidia).

**Recently many fake websites exist on Google when you search “fooocus”. Do not trust those – here is the only official source of Fooocus.**

# Project Status: Limited Long-Term Support (LTS) with Bug Fixes Only

The Fooocus project, built entirely on the **Stable Diffusion XL** architecture, is now in a state of limited long-term support (LTS) with bug fixes only. As the existing functionalities are considered as nearly free of programmartic issues (Thanks to [mashb1t](https://github.com/mashb1t)'s huge efforts), future updates will focus exclusively on addressing any bugs that may arise. 

**There are no current plans to migrate to or incorporate newer model architectures.** However, this may change during time with the development of open-source community. For example, if the community converge to one single dominant method for image generation (which may really happen in half or one years given the current status), Fooocus may also migrate to that exact method.

For those interested in utilizing newer models such as **Flux**, we recommend exploring alternative platforms such as [WebUI Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) (also from us), [ComfyUI/SwarmUI](https://github.com/comfyanonymous/ComfyUI). Additionally, several [excellent forks of Fooocus](https://github.com/lllyasviel/Fooocus?tab=readme-ov-file#forks) are available for experimentation.

Again, recently many fake websites exist on Google when you search “fooocus”. Do **NOT** get Fooocus from those websites – this page is the only official source of Fooocus. We never have any website like such as “fooocus.com”, “fooocus.net”, “fooocus.co”, “fooocus.ai”, “fooocus.org”, “fooocus.pro”, “fooocus.one”. Those websites are ALL FAKE. **They have ABSOLUTLY no relationship to us. Fooocus is a 100% non-commercial offline open-source software.**

# Features

Below is a quick list using Midjourney's examples:

| Midjourney | Fooocus |
| - | - |
| High-quality text-to-image without needing much prompt engineering or parameter tuning. <br> (Unknown method) | High-quality text-to-image without needing much prompt engineering or parameter tuning. <br> (Fooocus has an offline GPT-2 based prompt processing engine and lots of sampling improvements so that results are always beautiful, no matter if your prompt is as short as “house in garden” or as long as 1000 words) |
| V1 V2 V3 V4 | Input Image -> Upscale or Variation -> Vary (Subtle) / Vary (Strong)|
| U1 U2 U3 U4 | Input Image -> Upscale or Variation -> Upscale (1.5x) / Upscale (2x) |
| Inpaint / Up / Down / Left / Right (Pan) | Input Image -> Inpaint or Outpaint -> Inpaint / Up / Down / Left / Right <br> (Fooocus uses its own inpaint algorithm and inpaint models so that results are more satisfying than all other software that uses standard SDXL inpaint method/model) |
| Image Prompt | Input Image -> Image Prompt <br> (Fooocus uses its own image prompt algorithm so that result quality and prompt understanding are more satisfying than all other software that uses standard SDXL methods like standard IP-Adapters or Revisions) |
| --style | Advanced -> Style |
| --stylize | Advanced -> Advanced -> Guidance |
| --niji | [Multiple launchers: "run.bat", "run_anime.bat", and "run_realistic.bat".](https://github.com/lllyasviel/Fooocus/discussions/679) <br> Fooocus support SDXL models on Civitai <br> (You can google search “Civitai” if you do not know about it) |
| --quality | Advanced -> Quality |
| --repeat | Advanced -> Image Number |
| Multi Prompts (::) | Just use multiple lines of prompts |
| Prompt Weights | You can use " I am (happy:1.5)". <br> Fooocus uses A1111's reweighting algorithm so that results are better than ComfyUI if users directly copy prompts from Civitai. (Because if prompts are written in ComfyUI's reweighting, users are less likely to copy prompt texts as they prefer dragging files) <br> To use embedding, you can use "(embedding:file_name:1.1)" |
| --no | Advanced -> Negative Prompt |
| --ar | Advanced -> Aspect Ratios |
| InsightFace | Input Image -> Image Prompt -> Advanced -> FaceSwap |
| Describe | Input Image -> Describe |

Below is a quick list using LeonardoAI's examples:

| LeonardoAI | Fooocus |
| - | - |
| Prompt Magic | Advanced -> Style -> Fooocus V2 |
| Advanced Sampler Parameters (like Contrast/Sharpness/etc) | Advanced -> Advanced -> Sampling Sharpness / etc |
| User-friendly ControlNets | Input Image -> Image Prompt -> Advanced |

Also, [click here to browse the advanced features.](https://github.com/lllyasviel/Fooocus/discussions/117)

# Download

### Windows

You can directly download Fooocus with:

**[>>> Click here to download <<<](https://github.com/lllyasviel/Fooocus/releases/download/v2.5.0/Fooocus_win64_2-5-0.7z)**

After you download the file, please uncompress it and then run the "run.bat".

![image](https://github.com/lllyasviel/Fooocus/assets/19834515/c49269c4-c274-4893-b368-047c401cc58c)

The first time you launch the software, it will automatically download models:

1. It will download [default models](#models) to the folder "Fooocus\models\checkpoints" given different presets. You can download them in advance if you do not want automatic download.
2. Note that if you use inpaint, at the first time you inpaint an image, it will download [Fooocus's own inpaint control model from here](https://huggingface.co/lllyasviel/fooocus_inpaint/resolve/main/inpaint_v26.fooocus.patch) as the file "Fooocus\models\inpaint\inpaint_v26.fooocus.patch" (the size of this file is 1.28GB).

After Fooocus 2.1.60, you will also have `run_anime.bat` and `run_realistic.bat`. They are different model presets (and require different models, but they will be automatically downloaded). [Check here for more details](https://github.com/lllyasviel/Fooocus/discussions/679).

After Fooocus 2.3.0 you can also switch presets directly in the browser. Keep in mind to add these arguments if you want to change the default behavior:
* Use `--disable-preset-selection` to disable preset selection in the browser.
* Use `--always-download-new-model` to download missing models on preset switch. Default is fallback to `previous_default_models` defined in the corresponding preset, also see terminal output.

![image](https://github.com/lllyasviel/Fooocus/assets/19834515/d386f817-4bd7-490c-ad89-c1e228c23447)

If you already have these files, you can copy them to the above locations to speed up installation.

Note that if you see **"MetadataIncompleteBuffer" or "PytorchStreamReader"**, then your model files are corrupted. Please download models again.

Below is a test on a relatively low-end laptop with **16GB System RAM** and **6GB VRAM** (Nvidia 3060 laptop). The speed on this machine is about 1.35 seconds per iteration. Pretty impressive – nowadays laptops with 3060 are usually at very acceptable price.

![image](https://github.com/lllyasviel/Fooocus/assets/19834515/938737a5-b105-4f19-b051-81356cb7c495)

Besides, recently many other software report that Nvidia driver above 532 is sometimes 10x slower than Nvidia driver 531. If your generation time is very long, consider download [Nvidia Driver 531 Laptop](https://www.nvidia.com/download/driverResults.aspx/199991/en-us/) or [Nvidia Driver 531 Desktop](https://www.nvidia.com/download/driverResults.aspx/199990/en-us/).

Note that the minimal requirement is **4GB Nvidia GPU memory (4GB VRAM)** and **8GB system memory (8GB RAM)**. This requires using Microsoft’s Virtual Swap technique, which is automatically enabled by your Windows installation in most cases, so you often do not need to do anything about it. However, if you are not sure, or if you manually turned it off (would anyone really do that?), or **if you see any "RuntimeError: CPUAllocator"**, you can enable it here:

<details>
<summary>Click here to see the image instructions. </summary>

![image](https://github.com/lllyasviel/Fooocus/assets/19834515/2a06b130-fe9b-4504-94f1-2763be4476e9)

**And make sure that you have at least 40GB free space on each drive if you still see "RuntimeError: CPUAllocator" !**

</details>

Please open an issue if you use similar devices but still cannot achieve acceptable performances.

Note that the [minimal requirement](#minimal-requirement) for different platforms is different.

See also the common problems and troubleshoots [here](troubleshoot.md).

### Colab

(Last tested - 2024 Aug 12 by [mashb1t](https://github.com/mashb1t))

| Colab | Info
| --- | --- |
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lllyasviel/Fooocus/blob/main/fooocus_colab.ipynb) | Fooocus Official

In Colab, you can modify the last line to `!python entry_with_update.py --share --always-high-vram` or `!python entry_with_update.py --share --always-high-vram --preset anime` or `!python entry_with_update.py --share --always-high-vram --preset realistic` for Fooocus Default/Anime/Realistic Edition.

You can also change the preset in the UI. Please be aware that this may lead to timeouts after 60 seconds. If this is the case, please
