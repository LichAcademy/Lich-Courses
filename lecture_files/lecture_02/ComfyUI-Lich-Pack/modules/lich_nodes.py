from folder_paths import get_filename_list
from nodes import VAELoader


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


# Lecture 2: Custom Nodes Part II


# class WidgetInputs:
#     @classmethod
#     def INPUT_TYPES(cls):

#         ckp_list = folder_paths.get_filename_list("checkpoints")
#         lora_list = folder_paths.get_filename_list("loras")
#         cn_list = folder_paths.get_filename_list("controlnet")
#         # Note that there is inconsistency with noun numbers:
#         # checkpointS, loraS, (..., configS, style_modelS, embeddingS, diffuserS, ...) and controlnet (singular, not plural)

#         vae_list = core.VAELoader.vae_list()

#         data_in = {
#             "required": {
#                 "my_own_type": ("MY_OWN_TYPE",),
#                 "int_list": ([1, 2, 3],),
#                 "checkpoint": (ckp_list,),
#                 "LoRA": (lora_list,),
#                 "controlnet": (cn_list,),
#                 "vae": (vae_list,),
#             },
#         }

#         return data_in

#     RETURN_TYPES = ()
#     FUNCTION = "doNothing"
#     CATEGORY = "💀 Lich Nodes"

#     def doNothing(self):
#         return ()
