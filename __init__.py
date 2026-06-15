import torch

class AdvancedPrecisionCast:
    def __init__(self):
        pass
        
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "target_precision": (["float32", "float16", "bfloat16"], {"default": "float32"}),
                "force_alpha_remove": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "process_precision"
    CATEGORY = "utils/precision"

    def process_precision(self, image, target_precision, force_alpha_remove):
        # 1. Handle Alpha channel removal to prevent canvas shape mismatches
        if force_alpha_remove and image.shape[-1] == 4:
            image = image[..., :3]
            
        # 2. Map string dropdown selection to actual PyTorch data types
        dtype_map = {
            "float32": torch.float32,
            "float16": torch.float16,
            "bfloat16": torch.bfloat16
        }
        
        target_dtype = dtype_map.get(target_precision, torch.float32)
        
        # 3. Cast the tensor across memory lines safely
        casted_image = image.to(dtype=target_dtype)
        return (casted_image,)

class TensorDataTypeReporter:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING",)
    RETURN_NAMES = ("image", "data_type_info",)
    FUNCTION = "report_type"
    CATEGORY = "utils/precision"

    def report_type(self, image):
        # Extract the exact shape and technical scalar type of the incoming image data
        dtype_info = f"DataType: {image.dtype} | Shape: {list(image.shape)}"
        print(f"\n[Precision-SC Report] {dtype_info}\n")
        return (image, dtype_info,)


# Global node registrations
NODE_CLASS_MAPPINGS = {
    "CastImagePrecision": AdvancedPrecisionCast,  # Keeps your advanced code logic
    "ImageDataTypeReporter": TensorDataTypeReporter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CastImagePrecision": "Cast Image Precision",
    "ImageDataTypeReporter": "Image Data Type Reporter"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']