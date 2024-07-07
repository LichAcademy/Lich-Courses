from folder_paths import get_filename_list
from nodes import VAELoader

from nodes import (
    CheckpointLoaderSimple,
    CLIPTextEncode,
    CLIPSetLastLayer,
    EmptyLatentImage,
)


# Lecture 1: Creating Custom Nodes


class NothingNode:
    @classmethod
    def INPUT_TYPES(cls):
        data_in = {"required": {"image": ("IMAGE",)}}
        return data_in

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "doNothing"
    CATEGORY = "💀 Lich Nodes"

    def doNothing(self, image):
        outputImage = image
        return (outputImage,)


# Assignment 1 Solution


class ToLichPipe:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "vae": ("VAE",),
                "pos_cond": ("CONDITIONING",),
                "neg_cond": ("CONDITIONING",),
                "latent": ("LATENT",),
                "image": ("IMAGE",),
                "mask": ("MASK",),
                "controlnet": ("CONTROL_NET",),
            }
        }

    RETURN_TYPES = ("LICH_PIPE",)
    RETURN_NAMES = ("lich_pipe",)
    FUNCTION = "toLichPipe"
    CATEGORY = "💀 Lich Nodes"

    def toLichPipe(
        self, model, clip, vae, pos_cond, neg_cond, latent, image, mask, controlnet
    ):
        lich_pipe = (
            model,
            clip,
            vae,
            pos_cond,
            neg_cond,
            latent,
            image,
            mask,
            controlnet,
        )
        return (lich_pipe,)


class FromLichPipe:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "lich_pipe": ("LICH_PIPE",),
            }
        }

    RETURN_TYPES = (
        "MODEL",
        "CLIP",
        "VAE",
        "CONDITIONING",
        "CONDITIONING",
        "LATENT",
        "IMAGE",
        "MASK",
        "CONTROL_NET",
    )

    RETURN_NAMES = (
        "model",
        "clip",
        "vae",
        "pos_cond",
        "neg_cond",
        "latent",
        "image",
        "mask",
        "controlnet",
    )

    FUNCTION = "fromLichPipe"
    CATEGORY = "💀 Lich Nodes"

    def fromLichPipe(self, lich_pipe):
        (model, clip, vae, pos_cond, neg_cond, latent, image, mask, controlnet) = (
            lich_pipe
        )
        return (model, clip, vae, pos_cond, neg_cond, latent, image, mask, controlnet)


# Lecture 2: Widget Inputs


class WidgetInputs:
    @classmethod
    def INPUT_TYPES(cls):

        ckp_list = get_filename_list("checkpoints")
        lora_list = get_filename_list("loras")
        cn_list = get_filename_list("controlnet")
        vae_list = VAELoader.vae_list()

        data_in = {
            "required": {
                "checkpoints": (ckp_list,),
                "loras": (lora_list,),
                "controlnet": (cn_list,),
                "vae": (vae_list,),
            },
        }

        return data_in

    RETURN_TYPES = ()
    FUNCTION = "doNothing"
    CATEGORY = "💀 Lich Nodes"

    def doNothing(self):
        return ()


# Lecture 3: Primitive Inputs


class PrimitiveInputs:
    @classmethod
    def INPUT_TYPES(cls):
        data_in = {
            "required": {
                "default_int": ("INT", {}),
                "bounded_range": (
                    "INT",
                    {
                        "default": 3,
                        "min": -10,
                        "max": 10,
                        "step": 1,
                    },
                ),
                "even": (
                    "INT",
                    {
                        "default": 3,
                        "min": 1,
                        "max": 35,
                        "step": 8,
                    },
                ),
                "seed": (
                    "INT",
                    {
                        "default": 0,
                        "min": 0,
                        "max": 0xFFFFFFFFFFFFFFFF,
                        "step": 1,
                    },
                ),
                "float_in": (
                    "FLOAT",
                    {
                        "default": 0.0,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.1,
                    },
                ),
                "simple_str": (
                    "STRING",
                    {
                        "default": "hello",
                    },
                ),
                "longer_str": (
                    "STRING",
                    {
                        "multiline": True,
                        "dynamicPrompts": True,
                    },
                ),
                "switch": ("BOOLEAN", {"default": True}),
                "alignment": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "label_on": "Good",
                        "label_off": "Evil",
                    },
                ),
            }
        }
        return data_in

    RETURN_TYPES = ()
    FUNCTION = "doNothing"
    CATEGORY = "💀 Lich Nodes"

    def doNothing(self):
        return ()


# Some useful imports:

# from comfy.samplers import SAMPLER_NAMES as SAMPLERS
# from comfy.samplers import SCHEDULER_NAMES as SCHEDULERS
# from nodes import MAX_RESOLUTION


#    Assignment 3    #
#    ------------    #

# Your assignment is to design a node called Dream Loader, which seeks and loads DreamShaper checkpoint. Use what you have learned today to set up text widgets for prompt input. Aspect ratio should not be numerical, but implemented via widget that lets users choose between Portrait, Landscape or Square.

# Clip Skip is implemented as Boolean widget. It should be switched off by default, but if you toggle it on, it sets the last layer to -2, and modify the CLIP internally. And lastly, you are to package MODEL, CLIP, VAE, and the two conditionings into a basic_pipe data structure, compatible with Impact Pack nodes. Make sure it works by combining it with


#    Assignment 3: Solution    #
#    ----------------------    #


class DreamLoader:
    @classmethod
    def INPUT_TYPES(cls):
        data_in = {
            "required": {
                "positive": (
                    "STRING",
                    {
                        "multiline": True,
                        "dynamicPrompts": True,
                    },
                ),
                "negative": (
                    "STRING",
                    {
                        "multiline": True,
                        "dynamicPrompts": True,
                    },
                ),
                "aspect_ratio": (["Portrait", "Landscape", "Square"],),
                "clip_skip": ("BOOLEAN", {"default": False}),
            }
        }
        return data_in

    # Return types: BASIC_PIPE and LATENT
    RETURN_TYPES = ("BASIC_PIPE", "LATENT")

    # We use RETURN_NAMES this to rename the slot labels to lowercase: basic_pipe and latent. This is optional.
    RETURN_NAMES = ("basic_pipe", "latent")

    # The FUNCTION name is used to call the function that will be executed when the node is run.
    FUNCTION = "load_dreamshaper"
    CATEGORY = "💀 Lich Nodes"

    # The load_dreamshaper function is the core of the node. It takes the input data and returns the output data. Note that the function is a method of the class, so it takes 'self' as the first argument. The input data is passed as arguments to the function, and argument names must match the keys in the INPUT_TYPES dictionary.
    def load_dreamshaper(self, positive, negative, clip_skip, aspect_ratio):
        # The ckp_string is the path to the checkpoint file. You can change this to load a different checkpoint, or seek a different folder. I am on Windows 11, and path below correlates to absolute path "C:\comfyshared\models\checkpoints\SD1.5\dreamshaper_8.safetensors", with the root folder being base_path: "C:\comfyshared" (see extra_model_paths.yaml).
        ckp_string = "SD1.5/dreamshaper_8.safetensors"  # Note that Python prefers forward slashes, even on Windows.

        # We instantiate the classes we need to load the checkpoint, set the last layer of CLIP, encode the text, and generate an empty latent image.
        ckpt_loader_instance = CheckpointLoaderSimple()
        clip_skip_instance = CLIPSetLastLayer()
        text_to_cond_instance = CLIPTextEncode()
        empty_latent_instance = EmptyLatentImage()

        # Load the checkpoint. This returns the model, clip, and vae.
        (model, clip, vae) = ckpt_loader_instance.load_checkpoint(ckp_string)

        # Check if the user has toggled on clip_skip, and set the last layer to -2
        if clip_skip is True:
            (clip,) = clip_skip_instance.set_last_layer(clip, -2)

        # Encode the positive and negative text prompts. This is how we get the conditioning tensors.
        (pos_cond,) = text_to_cond_instance.encode(clip, positive)
        (neg_cond,) = text_to_cond_instance.encode(clip, negative)

        # Generate an empty latent image based on the aspect ratio chosen by the user.
        if aspect_ratio == "Portrait":
            (latent,) = empty_latent_instance.generate(432, 768, 1)

        elif aspect_ratio == "Landscape":
            (latent,) = empty_latent_instance.generate(768, 432, 1)

        elif aspect_ratio == "Square":
            (latent,) = empty_latent_instance.generate(512, 512, 1)

        # Package the model, clip, vae, positive conditioning, and negative conditioning into a basic_pipe data structure.
        basic_pipe = (model, clip, vae, pos_cond, neg_cond)

        # Return the basic_pipe and latent image.
        return (basic_pipe, latent)
