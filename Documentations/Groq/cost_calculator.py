def calculate_processing_cost(token_count, model_name, is_input=True):
    """
    Calculate the cost of processing tokens for a given model
    """
    # Price per million tokens (from the pricing table)
    model_prices = {
        "llama-3.2-1b": {"input": 0.04, "output": 0.04},
        "llama-3.1-70b": {"input": 0.59, "output": 0.79},
        "mixtral-8x7b": {"input": 0.24, "output": 0.24},
        "llama-3.2-90b-vision": {"input": 0.90, "output": 0.90}
    }
    
    if model_name not in model_prices:
        raise ValueError(f"Model {model_name} not found in pricing table")
    
    price_per_m = model_prices[model_name]["input" if is_input else "output"]
    cost = (token_count / 1_000_000) * price_per_m
    
    return cost

def print_cost_comparison(token_count):
    """Print cost comparison for different models"""
    models = ["llama-3.2-1b", "llama-3.1-70b", "mixtral-8x7b", "llama-3.2-90b-vision"]
    
    print(f"\nCost comparison for {token_count:,} tokens:")
    print("-" * 50)
    print(f"{'Model':<20} {'Input Cost':>15} {'Output Cost':>15}")
    print("-" * 50)
    
    for model in models:
        input_cost = calculate_processing_cost(token_count, model, is_input=True)
        output_cost = calculate_processing_cost(token_count, model, is_input=False)
        print(f"{model:<20} ${input_cost:>14.6f} ${output_cost:>14.6f}")

if __name__ == "__main__":
    # Example usage with different token counts
    token_counts = [1000, 10000, 100000, 1000000]
    
    for tokens in token_counts:
        print_cost_comparison(tokens)
