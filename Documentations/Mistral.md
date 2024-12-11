# Mistral AI

## Overview
Mistral AI is a French artificial intelligence company founded in 2023 by former DeepMind and Meta AI researchers. The company focuses on developing open-source large language models and has quickly gained recognition for their high-performance, efficient models.

## Mistral Models with Features

| Model | Features |
|---|---|
| Mistral-7B-v0.1 | - 32k vocabulary size\n- Rope Theta = 1e4\n- With sliding window |
| Mistral-7B-Instruct-v0.2 | - 32k vocabulary size\n- Rope Theta = 1e6\n- No sliding window |
| Mistral-7B-v0.3 | - Extended vocabulary to 32768 |
| Mistral-7B-Instruct-v0.3 | - Extended vocabulary to 32768\n- Supports v3 Tokenizer\n- Supports function calling |
| Mixtral-8x7B-v0.1 | - 32k vocabulary size\n- Rope Theta = 1e6 |
| Mixtral-8x7B-Instruct-v0.1 | - 32k vocabulary size\n- Rope Theta = 1e6 |
| Mixtral-8x7B-v0.3 | - Extended vocabulary to 32768\n- Supports v3 Tokenizer |
| Mixtral-8x7B-Instruct-v0.3 | - Extended vocabulary to 32768\n- Supports v3 Tokenizer\n- Supports function calling |
| Mixtral-8x22B-v0.1 | - 32k vocabulary size |
| Mixtral-8x22B-Instruct-v0.1 |  | 
| Mixtral-8x22B-Instruct-v0.3 | - 32768 vocabulary size |
| Mixtral-8x22B-v0.3 | - 32768 vocabulary size\n- Supports v3 Tokenizer |
| Codestral-22B-v0.1 | - 32768 vocabulary size\n- Supports v3 Tokenizer |
| Codestral-Mamba-7B-v0.1 | - 32768 vocabulary size\n- Supports v3 Tokenizer |
| Mathstral-7B-v0.1 | - 32768 vocabulary size\n- Supports v3 Tokenizer |
| Mistral-Nemo-Base-2407 | - 131k vocabulary size\n- Supports v3 tekken.json tokenizer |
| Mistral-Nemo-Instruct-2407 | - 131k vocabulary size\n- Supports v3 tekken.json tokenizer\n- Supports function calling |
| Mistral-Large-Instruct-2407 | - 32768 vocabulary size\n- Supports v3 Tokenizer\n- Supports function calling |
| Pixtral-2409 | - 131k vocabulary size\n- Supports v3 tekken.json tokenizer\n- Supports function calling |
| Mistral-Small-Instruct-2409 | - 32768 vocabulary size\n- Supports v3 Tokenizer\n- Supports function calling |
| Ministral-8B-Instruct-2410 | - 131k vocabulary size\n- Supports v3 tekken.json tokenizer\n- Supports function calling |
| Mistral-Large-Instruct-2411 | - 32768 vocabulary size\n- Supports v7 tokenizer\n- Supports function calling |
| Pixtral-Large-Instruct-2411 | - 32768 vocabulary size\n- Supports v7 tokenizer\n- Supports function calling |

## Mistral Model Sizes

*Note:*
- *BF16, or bfloat16 (short for Brain Floating Point 16), is a numerical data type used primarily in deep learning and machine learning applications. It is a variation of the standard 16-bit floating-point format that balances computational efficiency and precision.*
- *FP8 refers to an 8-bit floating-point format that is being adopted for specialized machine learning and AI tasks. It provides even more efficient computation and memory savings compared to formats like BF16 or FP32. Several versions of FP8 exist, depending on the specific needs of the application. These are typically defined by variations in how the available 8 bits are allocated between the sign, exponent, and mantissa (fraction).*

|Name|Number of parameters|Number of active parameters|Min. GPU RAM for inference (bf16)|Min. GPU RAM for inference (fp8)|
|:---|:---|:---|:---|:---|
|Mistral-7B-v0.3|7.3B|7.3B|16||
|Mixtral-8x7B-v0.1|46.7B|12.9B|100||
|Mixtral-8x22B-v0.3|140.6B|39.1B|300||
|Codestral-22B-v0.1|22.2B|22.2B|60||
|Codestral-Mamba-7B-v0.1|7.3B|7.3B|16||
|Mathstral-7B-v0.1|7.3B|7.3B|16||
|Mistral-Nemo-Instruct-2407|12B|12B|28|16|
|Mistral-Large-Instruct-2407|123B|123B|250||
|Pixtral-2409|12B|12B|28|16|
|Mistral-Small-2409|22B|22B|60||
|Ministral-8B-2410|8B|8B|24||
|Mistral-Large-Instruct-2411|123B|123B|250||
|Pixtral-Large-Instruct-2411|124B|124B|250||


## Pricing

