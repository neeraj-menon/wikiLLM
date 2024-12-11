# Groq


## Overview
Groq is a technology company known for its innovative approach to designing and building high-performance processors and systems for AI and machine learning workloads. Their focus is on delivering unparalleled speed and efficiency in data processing.

## Language Models Available on Groq with the Context Windows

| Model ID | Owned By | Context Window |
|---|---|---|
| llama3-groq-70b-8192-tool-use-preview | Groq | 8192 |
| gemma2-9b-it | Google | 8192 |
| llama3-8b-8192 | Meta | 8192 |
| llama-3.2-90b-vision-preview | Meta | 8192 |
| llama3-70b-8192 | Meta | 8192 |
| llama-3.2-11b-vision-preview | Meta | 8192 |
| llama-3.2-11b-text-preview | Meta | 8192 |
| whisper-large-v3-turbo | OpenAI | 448 |
| llava-v1.5-7b-4096-preview | Other | 4096 |
| llama-3.1-70b-versatile | Meta | 32768 |
| llama-3.2-3b-preview | Meta | 8192 |
| whisper-large-v3 | OpenAI | 448 |
| llama-guard-3-8b | Meta | 8192 |
| mixtral-8x7b-32768 | Mistral AI | 32768 |
| gemma-7b-it | Google | 8192 |
| distil-whisper-large-v3-en | Hugging Face | 448 |
| llama-3.2-1b-preview | Meta | 8192 |
| llama-3.2-90b-text-preview | Meta | 8192 |
| llama3-groq-8b-8192-tool-use-preview | Groq | 8192 |
| llama-3.1-8b-instant | Meta | 131072 |

## Groq Rate Limits (Free Plan)

### Chat Completions

| Model ID | Requests per minute | Requests per day | Tokens per minute | Tokens per day |
|---|---|---|---|---|
| gemma-7b-it | 30 | 14,400 | 15,000 | 500,000 |
| gemma2-9b-it | 30 | 14,400 | 15,000 | 500,000 |
| Ilama-3.1-70b-versatile | 30 | 14,400 | 6,000 | 200,000 |
| Ilama-3.1-8b-instant | 30 | 14,400 | 20,000 | 800,000 |
| Ilama-3.2-11b-text-preview | 30 | 7,000 | 7,000 | 500,000 |
| Ilama-3.2-11b-vision-preview | 30 | 7,000 | 7,000 | 500,000 |
| Ilama-3.2-1b-preview | 30 | 7,000 | 7,000 | 500,000 |
| Ilama-3.2-3b-preview | 30 | 7,000 | 7,000 | 500,000 |
| Ilama-3.2-90b-text-preview | 30 | 7,000 | 7,000 | 500,000 |
| Ilama-3.2-90b-vision-preview | 15 | 3,500 | 7,000 | 250,000 |
| Ilama-guard-3-8b | 30 | 14,400 | 15,000 | 500,000 |
| Ilama3-70b-8192 | 30 | 14,400 | 6,000 | 200,000 |
| Ilama3-8b-8192 | 30 | 14,400 | 30,000 | 500,000 |
| Ilama3-groq-70b-8192-tool-use-preview | 30 | 14,400 | 15,000 | 500,000 |
| Ilama3-groq-8b-8192-tool-use-preview | 30 | 14,400 | 15,000 | 500,000 |
| Ilava-v1.5-7b-4096-preview | 30 | 14,400 | 30,000 | 500,000 |
| mixtral-8×7b-32768 | 30 | 14,400 | 5,000 | 500,000 |

### Speech to Text

| Model ID | Requests per Minute | Requests per Day | Audio Seconds per Hour | Audio Seconds per Day |
|---|---|---|---|---|
| distil-whisper-large-v3-en | 20 | 2,000 | 7,200 | 28,800 |
| whisper-large-v3 | 20 | 2,000 | 7,200 | 28,800 |
| whisper-large-v3-turbo | 20 | 2,000 | 7,200 | 28,800 |

## Understanding Requests and Tokens

### What is a Request?
A request in the context of LLM APIs refers to a single call made to the API endpoint. Each time you send a prompt to the model and receive a response, that counts as one request. For example:
- Sending a message to generate text
- Asking the model to complete a code snippet
- Having a single turn in a conversation
- Processing an image (for multimodal models)

### What are Tokens?
Tokens are the fundamental units that language models use to process text. They represent pieces of words or characters that the model understands:
- A token can be as short as a single character or as long as a complete word
- On average, 1 token ≈ 4 characters in English text
- Common examples:
  - "hello" = 1 token
  - "understanding" = 2 tokens (usually split as "under" and "standing")
  - "AI" = 1 token
  - "1234" = 1 token

## Pricing

### Tokens-as-a-Service (Coming Soon)
(Developer Pay As You Go --per token)

### Understanding Groq's Tokens-as-a-Service

#### Key Features
- **Unprecedented Speed**: Groq's LPU™ (Language Processing Unit) delivers consistent, high-speed inference with speeds up to 128K tokens per second
- **Predictable Performance**: Unlike traditional GPU-based solutions, Groq provides consistent latency regardless of load
- **Cost-Effective Scaling**: Pay only for the tokens you process, with competitive pricing starting from $0.04 per million tokens

#### How Groq TaaS Works
1. **Token Processing**:
   - Input tokens are processed at the rates shown in the pricing table above
   - Different models offer different speed-cost tradeoffs
   - Token speeds are guaranteed and consistent

2. **Pricing Structure**:
   - Separate pricing for input and output tokens
   - Lower prices for smaller models (e.g., Llama 3.2 1B at $0.04/M tokens)
   - Premium pricing for larger, more capable models (e.g., Llama 3.1 70B at $0.59/M input tokens)

#### Advantages of Groq's TaaS
- **Speed Advantage**: Up to 10x faster than traditional GPU-based solutions
- **Deterministic Performance**: Consistent token processing speeds regardless of workload
- **Flexible Integration**: RESTful API interface for easy integration into existing applications
- **Cost Transparency**: Clear per-token pricing with no hidden infrastructure costs

#### Use Cases
- High-throughput text generation
- Real-time conversational AI
- Large-scale document processing
- Multimodal applications (text + vision)
- Speech transcription and processing

### On-demand Pricing for Tokens-as-a-Service

| AI Model | Current Speed (Tokens/Second) | Input Token Price ($/M Tokens) | Output Token Price ($/M Tokens) |
|---|---|---|---|
| Llama 3.2 1B (Preview) | 8k | $0.04 | $0.04 |
| Llama 3.2 3B (Preview) | 8k | $0.06 | $0.06 |
| Llama 3.1 70B Versatile | 128k | $0.59 | $0.79 |
| Llama 3.1 8B Instant | 128k | $0.05 | $0.08 |
| Llama 3 70B | 8k | $0.59 | $0.79 |
| Llama 3 8B | 8k | $0.05 | $0.08 |
| Mixtral 8x7B Instruct | 32k | $0.24 | $0.24 |
| Gemma 7B 8k Instruct | 950 | $0.07 | $0.07 |
| Gemma 2 9B 8k | 500 | $0.20 | $0.20 |
| Llama 3 Groq 70B Tool Use Preview | 8k | $0.89 | $0.89 |
| Llama 3 Groq 8B Tool Use Preview | 8k | $0.19 | $0.19 |
| Llama Guard 3 8B | 8k | $0.20 | $0.20 |
| Llama 3.1 70B Speculative Decoding | 8k | $0.59 | $0.99 |

### Automatic Speech Recognition (ASR) Models

| AI Model | Speed Factor | Price ($/Hour Transcribed) |
|---|---|---|
| Whisper V3 Large | 189x | $0.111 |
| Whisper Large v3 Turbo | 216x | $0.04 |
| Distil-Whisper | 250x | $0.02 |

### Vision Models

| AI Model | Input Token Price ($/M Tokens) | Output Token Price ($/M Tokens) |
|---|---|---|
| Llama 3.2 11B Vision 8k (Preview) | $0.18 | $0.18 |
| Llama 3.2 90B Vision 8k (Preview) | $0.90 | $0.90 |

