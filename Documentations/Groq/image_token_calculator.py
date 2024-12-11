from PIL import Image
import os
import numpy as np

def calculate_image_tokens(image_path, model_name="llama-3.2-90b-vision-preview", patch_size=14):
    """
    Calculate tokens for an image using vision model parameters
    
    Args:
        image_path (str): Path to the image file
        model_name (str, optional): Name of the vision model. Defaults to Llama Vision.
        patch_size (int, optional): Size of image patches. Defaults to 14.
    
    Returns:
        dict: A dictionary containing token information, or None if processing fails
    """
    # Validate input
    if not image_path:
        print("Error: No image path provided")
        return None
    
    try:
        # Normalize path and check if file exists
        normalized_path = os.path.normpath(image_path)
        
        if not os.path.exists(normalized_path):
            print(f"Error: Image file not found at {normalized_path}")
            return None
        
        # Load and get image dimensions
        try:
            image = Image.open(normalized_path)
        except Exception as open_error:
            print(f"Error opening image: {open_error}")
            return None
        
        width, height = image.size
        
        # Ensure minimum image size
        if width < patch_size or height < patch_size:
            print(f"Error: Image too small. Minimum size is {patch_size}x{patch_size}")
            return None
        
        # Model-specific token configurations with actual token limits
        model_token_configs = {
            "llama-3.2-90b-vision-preview": {
                "patch_size": 14,
                "token_limit": 8192,  # From Groq.md context window
                "description": "Llama 3.2 90B Vision Preview Model"
            },
            "llama-3.2-11b-vision-preview": {
                "patch_size": 16,
                "token_limit": 8192,  # From Groq.md context window
                "description": "Llama 3.2 11B Vision Preview Model"
            },
            "llava-v1.5-7b-4096-preview": {
                "patch_size": 16,
                "token_limit": 4096,  # From Groq.md context window
                "description": "LLaVA 1.5 7B Vision Preview Model"
            },
            "default": {
                "patch_size": 14,
                "token_limit": 8192,  # Conservative default from Groq.md
                "description": "Default Vision Model"
            }
        }
        
        # Select model configuration
        model_config = model_token_configs.get(model_name, model_token_configs["default"])
        
        # Calculate number of patches
        patches_w = width // model_config["patch_size"]
        patches_h = height // model_config["patch_size"]
        total_patches = patches_w * patches_h
        
        # Calculate tokens 
        # Add 1 for [CLS] token
        total_tokens = total_patches + 1
        
        # Dynamically calculate tokens based on image size and patch size
        token_scaling_factor = 1.5  # Empirical scaling factor
        total_tokens = int(total_tokens * token_scaling_factor)
        
        # Calculate token difference from model limit
        token_limit = model_config["token_limit"]
        tokens_over_limit = max(0, total_tokens - token_limit)
        tokens_under_limit = max(0, token_limit - total_tokens)
        
        # Prepare detailed results with comprehensive information
        result = {
            "image_path": normalized_path,
            "model": {
                "name": model_name,
                "description": model_config["description"]
            },
            "dimensions": f"{width}x{height}",
            "patch_size": model_config["patch_size"],
            "patches": f"{patches_w}x{patches_h}",
            "total_patches": total_patches,
            "total_tokens": total_tokens,
            "token_limit": token_limit,
            "token_analysis": {
                "tokens_over_limit": tokens_over_limit,
                "tokens_under_limit": tokens_under_limit,
                "is_within_limit": total_tokens <= token_limit
            },
            "token_scaling_factor": token_scaling_factor
        }
        
        return result
    
    except Exception as e:
        print(f"Unexpected error processing image: {e}")
        return None

def format_token_analysis(image_tokens):
    """
    Format token analysis results
    """
    total_tokens = image_tokens['total_tokens']
    token_limit = image_tokens['token_limit']
    tokens_over_limit = image_tokens['token_analysis']['tokens_over_limit']
    
    return f"Total Tokens: {total_tokens}\nToken Limit: {token_limit}\nTokens Over Limit: {tokens_over_limit}"

def validate_image_tokens(image_path):
    """
    Validate and print image token information
    
    Args:
        image_path (str): Path to the image file
    
    Returns:
        dict or None: Token information, or None if processing fails
    """
    try:
        # Try multiple models
        models = ["llama-3.2-90b-vision-preview", "llama-3.2-11b-vision-preview", "llava-v1.5-7b-4096-preview", "default"]
        
        for model in models:
            try:
                image_tokens = calculate_image_tokens(image_path, model_name=model)
                if image_tokens:
                    # Print formatted analysis
                    print(format_token_analysis(image_tokens))
                    return image_tokens
            except Exception as model_error:
                print(f"Error with {model} model: {model_error}")
        
        print("Failed to process image with any model")
        return None
    
    except Exception as e:
        print(f"Validation error: {e}")
        return None

if __name__ == "__main__":
    # Example usage with different models and images
    test_images = [
        "image.png",  # Replace with actual image paths
        "test_image.jpg"
    ]
    
    for image_path in test_images:
        validate_image_tokens(image_path)
