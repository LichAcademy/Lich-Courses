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
