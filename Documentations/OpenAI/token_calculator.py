import tiktoken

def calculate_openai_tokens(text, model_name="gpt-4o"):
    """
    Calculate tokens for OpenAI models using tiktoken
    
    Args:
        text (str): Input text to tokenize
        model_name (str, optional): OpenAI model name. Defaults to GPT-4o.
    
    Returns:
        dict: Token calculation details
    """
    
    print("openai")

    
    # Model-specific token limits
    model_token_limits = {
        # GPT-4o models
        "gpt-4o": 128_000,
        "gpt-4o-2024-11-20": 128_000,
        "gpt-4o-2024-08-06": 128_000,
        "gpt-4o-2024-05-13": 128_000,
        "chatgpt-4o-latest": 128_000,
        
        # GPT-4o-mini models
        "gpt-4o-mini": 128_000,
        "gpt-4o-mini-2024-07-18": 128_000,
        
        # GPT-4 Turbo models
        "gpt-4-turbo": 128_000,
        "gpt-4-turbo-2024-04-09": 128_000,
        "gpt-4-turbo-preview": 128_000,
        "gpt-4-0125-preview": 128_000,
        "gpt-4-1106-preview": 128_000,
        
        # Classic GPT-4 models
        "gpt-4": 8_192,
        "gpt-4-0613": 8_192,
        "gpt-4-0314": 8_192,
        
        # GPT-3.5 Turbo models
        "gpt-3.5-turbo-0125": 16_385,
        "gpt-3.5-turbo": 16_385,
        "gpt-3.5-turbo-1106": 16_385,
        "gpt-3.5-turbo-instruct": 4_096
    }
    
    try:
        # Determine the encoding based on the model
        if model_name.startswith(("gpt-4", "gpt-3.5-turbo")):
            encoder = tiktoken.encoding_for_model(model_name)
        else:
            # Fallback to cl100k_base for newer or unknown models
            encoder = tiktoken.get_encoding("cl100k_base")
        
        tokens = encoder.encode(text)
        token_count = len(tokens)
        
        # Check token limit
        max_tokens = model_token_limits.get(model_name, 128_000)
        is_within_limit = token_count <= max_tokens
        
        return {
            "model": model_name,
            "token_count": token_count,
            "within_limit": is_within_limit,
            "max_tokens": max_tokens,
            "remaining_tokens": max_tokens - token_count if is_within_limit else 0,
            "encoding_used": str(encoder)
        }
    
    except Exception as e:
        print(f"Error counting tokens for {model_name}: {e}")
        return {
            "model": model_name,
            "token_count": 0,
            "within_limit": False,
            "max_tokens": model_token_limits.get(model_name, 128_000),
            "remaining_tokens": 0,
            "encoding_used": "Unknown"
        }

def calculate_openai_cost(token_count, model_name="gpt-4o", is_input=True, use_cached=False):
    """
    Calculate cost for OpenAI models based on token count
    
    Args:
        token_count (int): Number of tokens
        model_name (str, optional): OpenAI model name. Defaults to gpt-4o.
        is_input (bool, optional): Whether calculating input or output tokens. Defaults to True.
        use_cached (bool, optional): Whether using cached input. Defaults to False.
    
    Returns:
        dict: Cost calculation details
    """
    # Comprehensive pricing for OpenAI models based on OpenAI.md
    model_prices = {
        # GPT-4o Models
        "gpt-4o": {
            "input": 2.50 if not use_cached else 1.25,
            "output": 10.00
        },
        "gpt-4o-2024-11-20": {
            "input": 2.50 if not use_cached else 1.25,
            "output": 10.00
        },
        "gpt-4o-2024-08-06": {
            "input": 2.50 if not use_cached else 1.25,
            "output": 10.00
        },
        "gpt-4o-2024-05-13": {
            "input": 5.00 if not use_cached else 2.50,
            "output": 15.00
        },
        "gpt-4o-audio-preview": {
            "input": 2.50 if not use_cached else 0,
            "output": 10.00
        },
        
        # GPT-4o mini Models
        "gpt-4o-mini": {
            "input": 0.150 if not use_cached else 0.075,
            "output": 0.600
        },
        "gpt-4o-mini-2024-07-18": {
            "input": 0.150 if not use_cached else 0.075,
            "output": 0.600
        },
        
        # o1 Models
        "o1-preview": {
            "input": 15.00 if not use_cached else 7.50,
            "output": 60.00
        },
        "o1-preview-2024-09-12": {
            "input": 15.00 if not use_cached else 7.50,
            "output": 60.00
        },
        "o1-mini": {
            "input": 3.00 if not use_cached else 1.50,
            "output": 12.00
        },
        "o1-mini-2024-09-12": {
            "input": 3.00 if not use_cached else 1.50,
            "output": 12.00
        },
        
        # Fine-Tuning Models
        "gpt-4o-2024-08-06-ft": {
            "input": 3.750 if not use_cached else 1.875,
            "output": 15.000
        },
        "gpt-4o-mini-2024-07-18-ft": {
            "input": 0.300 if not use_cached else 0.150,
            "output": 1.200
        },
        "gpt-3.5-turbo-ft": {
            "input": 3.000,
            "output": 6.000
        },
        
        # Realtime API Models
        "gpt-4o-realtime-preview": {
            "input": 5.00 if not use_cached else 2.50,
            "output": 20.00
        },
        "gpt-4o-realtime-preview-2024-10-01": {
            "input": 5.00 if not use_cached else 2.50,
            "output": 20.00
        }
    }
    
    # Validate model and get pricing
    if model_name not in model_prices:
        raise ValueError(f"Model {model_name} not found in pricing table")
    
    # Determine price based on input/output and cached status
    price_per_m = model_prices[model_name]["input" if is_input else "output"]
    
    # Calculate cost per 1 Million Tokens
    cost = (token_count / 1_000_000) * price_per_m
    
    return {
        "model": model_name,
        "token_count": token_count,
        "is_input": is_input,
        "use_cached": use_cached,
        "price_per_million": price_per_m,
        "total_cost": cost
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
    print(f"Encoding Used: {token_info['encoding_used']}")

def print_cost_details(cost_info):
    """
    Print detailed cost information
    
    Args:
        cost_info (dict): Cost calculation details
    """
    print(f"Model: {cost_info['model']}")
    print(f"Token Count: {cost_info['token_count']}")
    print(f"Token Type: {'Input' if cost_info['is_input'] else 'Output'}")
    print(f"Cached: {cost_info['use_cached']}")
    print(f"Price per Million Tokens: ${cost_info['price_per_million']:.4f}")
    print(f"Total Cost: ${cost_info['total_cost']:.6f}")

if __name__ == "__main__":
    # Example usage
    sample_texts = [
        "Hello, this is a sample text to demonstrate token counting for OpenAI models.",
        "A longer text that might approach the token limit. " * 100
    ]
    
    models = [
        "gpt-4o",
        "gpt-4-turbo",
        "gpt-3.5-turbo",
        "gpt-4",
        "llama-3.2-1b",
        "llama-3.1-70b",
        "mixtral-8x7b",
        "llama-3.2-90b-vision"
    ]
    
    for text in sample_texts:
        print("\n--- Text Analysis ---")
        print(f"Text: {text[:50]}...")
        
        for model in models:
            # Calculate tokens
            token_info = calculate_openai_tokens(text, model)
            print(f"\nModel: {model}")
            print_token_details(token_info)
            
            # Calculate cost
            input_cost = calculate_openai_cost(token_info['token_count'], model, is_input=True)
            output_cost = calculate_openai_cost(token_info['token_count'], model, is_input=False)
            
            print("\nInput Cost:")
            print_cost_details(input_cost)
            print("\nOutput Cost:")
            print_cost_details(output_cost)
            print("-" * 40)
