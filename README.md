# Lich Academy

Hello, and welcome to **Lich Academy**!

This repository contains a growing, open-access curriculum for mastering generative AI: **ComfyUI**, **A1111**, Python programming and all things AI/ML.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [ComfyUI Crash Course (2024)](#comfyui-crash-course-2024)
  - [Topic 1: Fundamentals I](#topic-1-fundamentals-i)
  - [Topic 2: Fundamentals II](#topic-2-fundamentals-ii)
  - [Topic 3: Image Upscaling Algorithms](#topic-3-image-upscaling-algorithms)
  - [Topic 4: Masking Nodes \& Techniques](#topic-4-masking-nodes--techniques)
  - [Topic 5: Regional Prompting](#topic-5-regional-prompting)
  - [Topic 6: IP Adapter \& FaceID](#topic-6-ip-adapter--faceid)
- [Stable Diffusion 101](#stable-diffusion-101)
  - [Topic 1: Fundamentals](#topic-1-fundamentals)
- [Terms and Conditions](#terms-and-conditions)
- [About Me](#about-me)
- [License](#license)

## ComfyUI Crash Course (2024)

**ComfyUI** is a powerful and flexible node-based interface for Stable Diffusion and generative AI workflows. If you are just starting out, below you will find structured lessons with walkthrough videos and practical resources to guide your learning.

### Topic 1: Fundamentals I

- text2image
- outpainting
- inpainting
- detailing

[![Watch the video](.media/yt_thumbs/comfy_01.webp)](https://youtu.be/XIUwXbxBmUc)

**Links to Resources**

- [Masks](https://civitai.com/articles/8730/comfyui-crash-course-2024)
- [CyberRealistic v5](https://civitai.com/models/15003?modelVersionId=537505)
- [CyberRealistic Inpainting v5](https://civitai.com/models/15003?modelVersionId=560903)
- [Impact Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) custom nodes (install through [Manager](https://github.com/Comfy-Org/ComfyUI-Manager))

---

### Topic 2: Fundamentals II

- ComfyUI Workflow Execution
- ComfyUI and A1111 differences
  - Noise generation differences: GPU vs CPU
  - Weight normalization differences
- SEGS Education
- Traffic Cones

[![Watch the video](.media/yt_thumbs/comfy_02.webp)](https://youtu.be/9fL66UOQjQ0)

**Links to Resources**

- [Article Link (Civitai)](https://civitai.com/articles/8893)
- Checkpoint used in the video was [CyberRealistic](https://civitai.com/models/15003)

---

### Topic 3: Image Upscaling Algorithms

- Traditional Upscaling Algorithms
- AI Upscaling
- Latent Upscaling
- Input Nodes

[![Watch the video](.media/yt_thumbs/comfy_03.webp)](https://youtu.be/kl2U1z0yXTk)

**Links to Resources**

- [Article Link (Civitai)](https://civitai.com/articles/9102)
- Checkpoint used in the video was [CyberRealistic](https://civitai.com/models/15003)

---

### Topic 4: Masking Nodes & Techniques

- Constructing Masks
- Solid Mask
- Mask Composite
- Input Types:
  - Widget Inputs
  - Connection Inputs
- Converting Inputs
- Primitive Nodes and Primitive Data Types
- Grid Alignment (Snap-To-Grid)

[![Watch the video](.media/yt_thumbs/comfy_04.webp)](https://youtu.be/w7xXrcclqlA)

**Links to Resources**

- [Article Link (Civitai)](https://civitai.com/articles/9287)
- Checkpoint used in the video was [CyberRealistic](https://civitai.com/models/15003)

---

### Topic 5: Regional Prompting

- Regional Prompting
- Get/Set Nodes
- High Res Fix via Custom Scripts

[![Watch the video](.media/yt_thumbs/comfy_05.webp)](https://youtu.be/99Famd8Uyek)

**Links to Resources**

- [Article Link (Civitai)](https://civitai.com/articles/9534)
- Checkpoint used in the video was [CyberRealistic](https://civitai.com/models/15003)
- [Negative Hand](https://civitai.com/models/56519) (embedding)

---

### Topic 6: IP Adapter & FaceID

- IP Adapter
- FaceID
- Comfy Frontend Comparison: New vs Old

[![Watch the video](.media/yt_thumbs/comfy_06.webp)](https://youtu.be/bGCC5_vQ-bo)

**Links to Resources**

- [Article Link (Civitai)](https://civitai.com/articles/9826)
- [UP Adapter Bundle (Civitai)](https://civitai.com/models/907545/ip-adapter-bundle)
- Checkpoints used in the video:
  - [CyberRealistic](https://civitai.com/models/15003)
  - [RPG (by Anashel)](https://civitai.com/models/1116/)
- Image Credit: [Woman Holding Glass Terrarium (Juliana Stein/Pexels)](https://www.pexels.com/photo/woman-wearing-brown-long-sleeved-shirt-holding-round-glass-terrarium-2174676/)

## Stable Diffusion 101

### Topic 1: Fundamentals

[Lecture 1 Video](https://youtu.be/8QH-mzORYUU)

- You can download my slides [here](<Stable Diffusion 101/Topic 1 - Fundamentals/Slides/Topic 1 - Lecture - PDF.pdf>).

[Computer Lab 1 Video](https://youtu.be/RDuIeuOIB7s)

- You can download my slides [here](<Stable Diffusion 101/Topic 1 - Fundamentals/Slides/Topic 1 - Computer Lab - PDF.pdf>).

[Lecture Notes](<Stable Diffusion 101/Topic 1 - Fundamentals/Topic 1 - Fundamentals.md>)

If you are struggling with conda environments so much, that you are at a point of giving up, I have exported `py310`, `py311` and `comfy3d` environments for you (assuming you are on Windows machine, and have Nvidia graphics card with CUDA-compatible GPU). You can download them [here](<Stable Diffusion 101/Topic 1 - Fundamentals/Files/environments.zip>).

For example, to install `py310` environment, you can run:

```sh
conda env create --file py310.yaml
```

This is a handy way to back things up, but keep in mind that dependencies change over time, so it's always better to create your own environment from scratch.

## Terms and Conditions

This is the part ~~where I legally cover my...~~ you pinky-promise that:

- You won't use your newly-gained AI powers for evil;
- You won't blame me if you get caught by the AI police;
- You won't sue me if your PC turns you into a [paperclip](https://en.wikipedia.org/wiki/Instrumental_convergence#Paperclip_maximizer).

In all seriousness, I _am_ sharing my knowledge with you in good faith. I'm not responsible for any consequences of your actions. You're a grown-up, you can handle it. 🧙‍♂️

## About Me

Marko Zegarac (a.k.a. "Professor Lich")

I'm a former academic-turned-YouTuber, with passion for education. After leaving academic world, I created 'Professor Lich' online persona, YouTube channel and started building my own curriculum there.

I excel at breaking down complex ideas and presenting them in a simple, understandable manner. My goal is to make learning enjoyable and accessible to everyone, regardless of their age, gender, academic background or physical ability.

I believe that student debt is a serious issue, and I am committed to promoting free education. I envision a world where students can access high-quality educational content without paying with their money or their privacy. Education should not be a commodity where attention is monetized, but a fundamental right accessible to all.

Furthermore, I advocate for an accessible curriculum that can reach learners worldwide. With the power of AI, we can democratize knowledge and ensure that everyone has the opportunity to learn and grow.

Help me make education free, accessible, and enjoyable for all!

Linking to my YouTube channel would help me a lot. ❤️

YouTube: <https://www.youtube.com/channel/UCVFodFpogQKyXmbFlGZayhQ>

If you have a dollar to spare:

Patreon: <https://www.patreon.com/professorlich/>  
Ko-Fi: <https://ko-fi.com/professorlich>

## License

Until I figure out how to properly license it, I am keeping it as:

©️ 2024 Professor Lich: All Rights Reserved

If you have any suggestions, please let me know. 👍
