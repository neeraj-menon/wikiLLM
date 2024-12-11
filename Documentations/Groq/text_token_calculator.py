from transformers import AutoTokenizer
import tiktoken

def calculate_text_tokens(text, encoding_name="cl100k_base"):
    """Use tiktoken to calculate the number of tokens in a piece of text."""
    encoder = tiktoken.get_encoding(encoding_name)
    return len(encoder.encode(text))
