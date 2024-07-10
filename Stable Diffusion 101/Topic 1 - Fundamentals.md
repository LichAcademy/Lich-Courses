# Topic 1: Fundamentals (WORK IN PROGRESS)

## Conda Commands Overview

To create a new conda environment, you can use `create` command:

```sh
conda create --name py310
```

You will be prompted to confirm the creation of the new environment. You can skip the prompt by adding `--yes` flag. For example, let's create a new environment called `py311` and skip the prompt by adding `--yes`:

```sh
conda create --name py311 --yes
```

Conda environments can be activated using `activate` command:

```sh
conda activate py310
```

Normally, the name of the currently active environment is displayed in the brackets in terminal. However, there are situations where you might not see the environment name in the brackets (for example, VS Code terminal). In that case, you can use `conda env list` to list all available environments and find the one that is activated (marked with asterisk `*`).

```sh
conda env list
```

Once activated, any package you install will be going into the activated environment. Let's install Python 3.10.6 into the `py310` environment:

```sh
conda install python=3.10.6
```

You can also install packages into the environment without activating it. For example, to install Python 3.11.9 into the `py311` environment without activating it, you can use the following command:

```sh
conda install python=3.11.9 --name py311
```

If you are not sure how to spell the package name, or want to see the package versions available, you can use `search` command:

```sh
conda search python
```

This command allows the use of wildcards. For example, to search for all available versions of Python 3.10, you can use:

```sh
conda search python=3.10*
```

And lastly, to remove an environment, you can use `remove` command:

```sh
conda remove --name py311 --all
```

Flag `--all` removes all the packages in the environment, and the environment itself. If you want to keep the environment but remove all the packages, you can use `--all` flag without the environment name:

```sh
conda remove --all
```

If you don't include `--all` flag:

```sh
conda remove --name py311
```

Conda will prompt you to specify which package you wish to remove from `py311` environment. 

### Installing Packages

To install packages, use `install` command:

```sh
conda install python=3.10.6
```

As with creation of environments, you can skip the prompt by adding `--yes` flag:

```sh
conda install python=3.11.9 --yes
```

Just as we have used `conda env list` to list all available environments, you can use `conda list` to list all packages installed in the currently active environment:

```sh
conda list
```

## Stable Diffusion WebUI Setup (Automatic1111)

```sh
conda create --name py310

conda activate py310

conda install python=3.10.6
```

### Creating `py311`

```sh
conda create --name py311 --yes

conda activate py311

conda install python=3.11.9 --yes
```

### Creating `kohya`

```sh
conda create --name kohya --yes

conda activate kohya

conda install python=3.10.11 --yes

conda install cuda --channel nvidia/label/cuda-11.8.0 --yes
```

### Assignment Solution

Note: This assignment assumes that you have Nvidia graphics card with CUDA-compatible GPU.

#### Step 1. Create Conda Environment

We create a new conda environment, and give it name `comfy3D`:

```sh
conda create --name comfy3D --yes
conda activate comfy3D
conda install python=3.11.9 --yes

# Or:
conda install python=3.11.9 --name comfy3D --yes
conda install python=3.11.9 --name comfy3D --yes
conda install cuda --channel nvidia/label/cuda-12.1.0 --channel nvidia/label/cuda-12.1.1 --name comfy3D --yes
```

Since repository requires CUDA 12.1, you were expected to do some research. Eventually, you would discover archived documentation page on Nvidia website regarding CUDA 12.1:

[Using Conda to Install the CUDA Software](https://docs.nvidia.com/cuda/archive/12.1.1/cuda-installation-guide-microsoft-windows/index.html#using-conda-to-install-the-cuda-software).

The command I used was:

```sh
conda install cuda --channel nvidia/label/cuda-12.1.0 --channel nvidia/label/cuda-12.1.1 --yes
```

Note that I am using official nvidia channel. If you went to Anaconda website, it is possible you discovered other channels offering the same package, in which case your command would look different. For purposes of this assignment, I don't think it matters which channel you use here.

```sh
git clone https://github.com/comfyanonymous/ComfyUI.git
```

```sh
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121
```

```sh
pip install -r requirements.txt
pip install -r requirements_post.txt
```

```sh
pip install -r requirements.txt
pip install -r requirements_post.txt
pip install xformers --index-url https://download.pytorch.org/whl/cu121
```

> ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
> torchaudio 2.3.1+cu121 requires torch==2.3.1+cu121, but you have torch 2.3.0+cu121 which is incompatible.
> torchvision 0.18.1+cu121 requires torch==2.3.1+cu121, but you have torch 2.3.0+cu121 which is incompatible.

I then fixed it using:

```sh
pip install torch==2.3.0+cu121 torchaudio==2.3.0+cu121 torchvision==0.18.0+cu121 --extra-index-url https://download.pytorch.org/whl/cu121
```

I then installed two more dependencies that developer did not include in the requirements.txt file:

```sh
pip install roma
pip install rembg
```

I have renamed the cloned folder into `Comfy-3D`, so that I have Automatic1111, ComfyUI and Comfy-3D projects all in the same location.

```sh
pip install -r requirements_post_win_py311_cu121.txt
```
