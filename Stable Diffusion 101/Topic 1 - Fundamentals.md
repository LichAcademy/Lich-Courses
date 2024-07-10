# Topic 1: Fundamentals (WORK IN PROGRESS)

## Table of Contents

- [Topic 1: Fundamentals (WORK IN PROGRESS)](#topic-1-fundamentals-work-in-progress)
  - [Table of Contents](#table-of-contents)
  - [Conda Commands](#conda-commands)
    - [Environments](#environments)
      - [Creating](#creating)
      - [Listing](#listing)
      - [Activating](#activating)
    - [Conda Packages](#conda-packages)
      - [Installing](#installing)
      - [Searching for Packages](#searching-for-packages)
      - [Listing Installed Packages](#listing-installed-packages)
      - [Deleting Packages](#deleting-packages)
    - [Delete Environment](#delete-environment)
  - [Stable Diffusion WebUI Setup (Automatic1111)](#stable-diffusion-webui-setup-automatic1111)
    - [Step 1. Create Conda Environment for A1111](#step-1-create-conda-environment-for-a1111)
    - [Step 2. Clone Repository](#step-2-clone-repository)
    - [Step 3. Set up Visual Studio Project](#step-3-set-up-visual-studio-project)
    - [Creating `py311`](#creating-py311)
    - [Creating `kohya`](#creating-kohya)
  - [Assignment Solution](#assignment-solution)
    - [Step 1. Create Conda Environment](#step-1-create-conda-environment)

## Conda Commands

### Environments

#### Creating

To create a new conda environment, you can use `create` command:

```sh
conda create --name py310
```

You will be prompted to confirm the creation of the new environment. You can skip the prompt by adding `--yes` flag. For example, let's create a new environment called `py311` and skip the prompt by adding `--yes`:

```sh
conda create --name py311 --yes
```

#### Listing

Normally, the name of the currently active environment is displayed in the brackets in terminal. However, there are situations where you might not see the environment name in the brackets (for example, VS Code terminal). In that case, you can use `conda env list` to list all available environments and find the one that is activated (marked with asterisk `*`).

```sh
conda env list
```

#### Activating

Conda environments can be activated using `activate` command:

```sh
conda activate py310
```

### Conda Packages

#### Installing

Once activated, any package you install will be going into the activated environment. To install packages, use `install` command:

```sh
conda activate py310 # Unless already activated
conda install python
```

As with creation of environments, you can answer affirmatively to all upcoming prompts by adding `--yes` flag:

```sh
conda install python=3.10.6 --yes
```

You can specify the version of the package you want to install. For example, to install `Python 3.10.6` into the `py310` environment, you can use the following command:

```sh
conda install python=3.10.6
```

You can also install packages into the environment without activating it. For example, to install `Python 3.11.9` into the `py311` environment without activating it, you can use the following command:

```sh
conda install python=3.11.9 --name py311
```

#### Searching for Packages

If you are not sure how to spell the package name, or want to see the package versions available, you can use `search` command:

```sh
conda search python

# Note that you can also use wildcards, if you are not sure about the exact package name:
conda search *ython
conda search python=3.10*
```

#### Listing Installed Packages

Just as we have used `conda env list` to list all available environments, you can use `conda list` to list all packages installed in the currently active environment:

```sh
conda list
```

#### Deleting Packages

To remove a package, for example, `cuda` from `py311` environment, you can use:

```sh
conda remove --name py311 cuda
```

### Delete Environment

To delete the environment along with all its packages, you can use `remove` command:

```sh
conda remove --name py311 --all
```

## Stable Diffusion WebUI Setup (Automatic1111)

### Step 1. Create Conda Environment for A1111

As you recall, Automatic1111 requires Python 3.10.6. Let's create a new environment called `py310` and install Python 3.10.6 into it:

```sh
conda create --name py310

conda activate py310

conda install python=3.10.6
```

### Step 2. Clone Repository

Assuming you have installed `git`, you can clone the repository. Easiest way is to navigate to the folder where you want to clone the repository, right-click and select `Git Bash Here` or `Open in Terminal`. Then you can use `git clone` command to clone the repository:

```sh
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
```

### Step 3. Set up Visual Studio Project

As shown in the video, you can open the folder in Visual Studio Code by right-clicking on the folder and selecting `Open in Visual Studio Code`. Alternatively, you can open the project by typing `code .` in the terminal (while inside the folder). Save the workspace by choosing `Save Workspace As...` from the `File` menu. This will create a `.code-workspace` file in the folder. You can then open the project by double-clicking on the `.code-workspace` file.

This file is actually a JSON file that contains various settings for the project. For example, if you open the `.code-workspace` file in a text editor, you will see something like this:

```json
{
    "folders": [
        {
            "path": "."
        }
    ],
    "settings": {}
}
```

You can edit this file.

```json
// Unlike JSON files, code-workspace files allow for comments. I will try to explain what I am doing and why.

// Any changes I make here won't impact your settings outside of this workspace.

{
    "folders": [
        {
            "path": "."
        }
    ],

    // The 'settings' object contains the settings that apply to the workspace.
    "settings": {
        "editor.fontSize": 16, // We increase the font size from 14 to 16 (just my personal preference)
        "editor.wordWrap": "on", // We enable 'word wrap' so that long lines of code are wrapped to the next line.
        "editor.defaultFormatter": "ms-python.black-formatter", // We set the default formatter to 'black', which is the name of a code formatter for Python.
        "editor.formatOnSave": true, // Each time you save, the code will be formatted.

        // Linters are tools that analyze your code to find errors and enforce coding standards.
        // These are some of the linting rules that I disabled for 'pylint' (Python Linter). Unless you are following my 'Learning Python with ComfyUI' tutorials, you don't need to worry about this bit.
        "pylint.args": [
            "--disable=unused-argument, redefined-outer-name, line-too-long, wrong-import-position, wrong-import-order, missing-module-docstring, missing-function-docstring, missing-class-docstring, invalid-name, consider-using-enumerate, too-many-locals, too-many-arguments, bad-classmethod-argument, import-outside-toplevel, unused-variable"
        ],
    },
    "extensions": {
        // To save you the trouble of searching for extensions, I have included a list of recommended extensions. You can install them by clicking on the 'Install' button that appears when you open this workspace.
        "recommendations": [
            "ms-python.debugpy",
            "donjayamanne.python-environment-manager",
            "ms-python.vscode-pylance",
            "ms-python.pylint",
            "ms-python.black-formatter",
            "nilssoderman.batch-runner",
            "ms-python.python",
            "equinusocio.vsc-material-theme-icons"
        ]
    }
}
```

The script that installs all the dependencies automatically is inside `webui-user.bat` file:

```bat
@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=

call webui.bat
```

However, before we run this script, let let me show you some useful arguments you can provide.

For example, this script automatically creates `venv` virtual environment. This is not an issue, although it does create environment within an environment unnecessarily. I will specify `-` as `VENV_DIR`.

Another thing that catches me every time, script downloads Stable Diffusion 1.5 base model. To opt-out, you need to add `--no-download-sd-model` to `COMMANDLINE_ARGS`.

```bat
@echo off

set PYTHON=
set GIT=
set VENV_DIR=-
set COMMANDLINE_ARGS=^
    --no-download-sd-model

call webui.bat
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

## Assignment Solution

Note: This assignment assumes that you have Nvidia graphics card with CUDA-compatible GPU.

### Step 1. Create Conda Environment

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

Clone ComfyUI repository:

```sh
git clone https://github.com/comfyanonymous/ComfyUI.git
```

Assuming you have Nvidia graphics card with CUDA-compatible GPU, you can install these dependencies:

```sh
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121
```

For the rest of the dependencies, you can use the provided `requirements.txt` file:

```sh
pip install -r requirements.txt
```

You Git-clone Comfy-3D repository:

And then you install the dependencies:

```sh
pip install -r requirements.txt
pip install -r requirements_post.txt
pip install xformers --index-url https://download.pytorch.org/whl/cu121
```

At this point, I have encountered an error telling me that `roma` and `rembg` are missing. It would seem that the developer did not include `roma` and `rembg` in the `requirements.txt` file. You can install them using:

```sh
pip install roma
pip install rembg
```

Now, you run `main.py`, and everything should work, right?

Nope. You will encounter another error:

> ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
> torchaudio 2.3.1+cu121 requires torch==2.3.1+cu121, but you have torch 2.3.0+cu121 which is incompatible.
> torchvision 0.18.1+cu121 requires torch==2.3.1+cu121, but you have torch 2.3.0+cu121 which is incompatible.

I resolved it using the following:

```sh
pip install torch==2.3.0+cu121 torchaudio==2.3.0+cu121 torchvision==0.18.0+cu121 --extra-index-url https://download.pytorch.org/whl/cu121
```

In hindsight, this 'assignment' was way too hard, especially for someone just starting out.
