import tiktoken

def calculate_anthropic_tokens(text, model_name="claude-3-5-sonnet-20241022"):
    """
    Calculate tokens for Anthropic models using tiktoken
    
    Args:
        text (str): Input text to tokenize
        model_name (str, optional): Anthropic model name. Defaults to latest Sonnet.
    
    Returns:
        dict: Token calculation details
    """
    
    print("anthropic")

    
    # Model-specific token limits
    model_token_limits = {
        "claude-3-5-sonnet-20241022": 200_000,
        "claude-3-opus": 200_000,
        "claude-3-sonnet": 200_000,
        "claude-3-haiku": 200_000
    }
    
    try:
        # Use cl100k_base encoding (same as GPT-4)
        encoder = tiktoken.get_encoding("cl100k_base")
        tokens = encoder.encode(text)
        token_count = len(tokens)
        
        # Check token limit
        max_tokens = model_token_limits.get(model_name, 200_000)
        is_within_limit = token_count <= max_tokens
        
        return {
            "model": model_name,
            "token_count": token_count,
            "within_limit": is_within_limit,
            "max_tokens": max_tokens,
            "remaining_tokens": max_tokens - token_count if is_within_limit else 0
        }
    
    except Exception as e:
        print(f"Error counting tokens for {model_name}: {e}")
        return {
            "model": model_name,
            "token_count": 0,
            "within_limit": False,
            "max_tokens": model_token_limits.get(model_name, 200_000),
            "remaining_tokens": 0
        }

def print_token_details(token_info):
    """
    Print detailed token information
    
    Args:
        token_info (dict): Token calculation details
    """
    print(f"Model: {token_info['model']}")
    print(f"Token Count: {token_info['token_count']}")
    print(f"Within Limit: {token_info['within_limit']}")
    print(f"Max Tokens: {token_info['max_tokens']}")
    print(f"Remaining Tokens: {token_info['remaining_tokens']}")

if __name__ == "__main__":
    # Example usage
    sample_texts = [
        "Hello, this is a sample text to demonstrate token counting for Claude models.",
        "A longer text that might approach the token limit. " * 100
    ]
    
    models = [
        "claude-3-5-sonnet-20241022",
        "claude-3-opus",
        "claude-3-sonnet",
        "claude-3-haiku"
    ]
    
    for text in sample_texts:
        print("\n--- Text Analysis ---")
        print(f"Text: {text[:50]}...")
        
        for model in models:
            token_info = calculate_anthropic_tokens(text, model)
            print(f"\nModel: {model}")
            print_token_details(token_info)
            print("-" * 40)
