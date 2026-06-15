# ComfyUI-PrecisionCast
<<<<<<< HEAD
A node that allows you to manually change image data precision formats (`Float32`, `Float16`, `BFloat16`) inside ComfyUI and view image data types for troubleshooting.
=======

This custom node pack allows you to manually change image data precision formats (`Float32`, `Float16`, `BFloat16`) inside ComfyUI and view image data types for troubleshooting.

## Why was this created?
Modern fast upscaling models (like `1xDeJPG_realplksr_otf`) output image data in `BFloat16` to maximize GPU speed. However, legacy nodes or nodes relying on NumPy/OpenCV (such as certain Color Correct or Bilateral Filter nodes) do not support 16-bit formats. When connected, they throw fatal crashes like `TypeError: Got unsupported ScalarType BFloat16` or OpenCV `(-210:Unsupported format...)`.

This node acts as a direct compatibility adapter to convert your data streams back to standard formats so different node packs can work together without crashing.

---

## 🛠️ How to Use & Node Guide

Both nodes can be found in the right-click menu under: **`utils/precision`**

### 1. Cast Image Precision
Place this node directly between the upscaler model causing the error and your targeted color/filtering node.
* **`target_precision`**: Choose `float32`, `float16`, or `bfloat16`. 
  * *To fix crashes:* Set this to `float32` right before your color correction or OpenCV-based nodes.
* **`force_alpha_remove` (`True`/`False`)**: 
  * **True (Recommended for video)**: Automatically strips out hidden transparency/alpha layers, changing images from RGBA to raw RGB. Leave this on `True` when processing digital video clips to prevent downstream video saving encoders from crashing due to unexpected empty alpha channels.
  * **False**: Passes the alpha channel through untouched.

### 2. Image Data Type Reporter
Place this node anywhere in your pipeline sequence. It acts as a passive pass-through that prints the exact data format (e.g., `torch.bfloat16`) and pixel dimensions of the image directly to your black ComfyUI terminal console window for debugging.

---

## 💾 Installation

Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```
Clone this repository:
```bash
git clone https://github.com
```
Restart your ComfyUI server to load the nodes.
>>>>>>> db3b66f (Initial commit of precision cast nodes and readme)
