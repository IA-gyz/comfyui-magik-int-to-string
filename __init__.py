"""Integer to zero-padded string conversion for ComfyUI."""


class MagikIntToString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("INT", {"default": 0}),
                "padding": ("INT", {"default": 3, "min": 1, "max": 99, "step": 1}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "convert"
    CATEGORY = "Magik/Utils"
    DESCRIPTION = "Converts an integer to a string with leading zeros up to the minimum width."

    def convert(self, value, padding=3):
        return (str(value).zfill(max(1, min(99, int(padding)))),)


NODE_CLASS_MAPPINGS = {"MagikIntToString": MagikIntToString}
NODE_DISPLAY_NAME_MAPPINGS = {"MagikIntToString": "Magik Int to String"}
