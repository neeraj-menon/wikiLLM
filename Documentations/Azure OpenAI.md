# Azure OpenAI

## Overview

Azure OpenAI is a suite of AI services for developers, including a powerful language model, a chat service, and a text embedding service. It is built on top of Azure Cognitive Services and is designed to be easy to use, scalable, and cost-effective for developers.

## Pricing

### o1 Preview

o1 is the new reasoning model series for complex tasks. The model has 128K context and an October 2023 knowledge cutoff.

| Model | Pricing (1M Tokens) |
|---|---|
| o1 | Global: Input: N/A Cached Input: \$7.50 Output: N/A |
|  | US/EU – Data Zones: Input: \$16.50 Cached Input: \$8.25 Output: \$66 |
|  | Regional: Input: N/A Cached Input: \$8.25 Output: N/A |

Plan with the [Pricing Calculator](https://gptforwork.com/tools/openai-chatgpt-api-pricing-calculator)

### o1 Mini

o1-mini is a fast, cost-efficient reasoning model tailored to coding, math, and science use cases. The model has 128K context and an October 2023 knowledge cutoff.

| Model | Pricing (1M Tokens) |
|---|---|
| o1-mini | Global: Input: N/A Cached Input: \$1.50 Output: N/A |
|  | US/EU – Data Zones: Input: \$3.30 Cached Input: \$1.65 Output: \$13.20 |
|  | Regional: Input: N/A Cached Input: \$1.65 Output: N/A |

Plan with the [Pricing Calculator](https://gptforwork.com/tools/openai-chatgpt-api-pricing-calculator)

### Realtime API

Featured in the Realtime API, the GPT-4o-Realtime-Preview supports multilingual speech-to-speech capabilities. Optimized for real-time, low-latency conversations, it enables natural interactions with minimal delay, ideal for chatbots and conversational AI.

| Model | Pricing (1M Tokens) |
|---|---|
| GPT-4o-Realtime-Preview-Global | Text: Input: \$5 Text Cached Input: \$2.75 Text Output: \$20 Audio: Input: \$100 Audio Cached Input: \$20 Audio Output: \$200 |
| GPT-4o-Realtime-Preview-US/EU – Data Zones | Text: Input: \$5.50 Text Cached Input: \$2.50 Text Output: \$22 Audio: Input: \$110 Audio Cached Input: \$22 Audio Output: \$220 |
| GPT-4o-Realtime-Preview-Regional | Text: Input: \$5.50 Text Cached Input: \$2.75 Text Output: \$22 Audio: Input: \$110 Audio Cached Input: \$22 Audio Output: \$220 |

### Chat Completions API - Coming soon

Featured in the Chat Completions API, the GPT 4o-Audio-Preview model processes and generates audio content. It supports advanced features like speech recognition and audio synthesis, ideal for asynchronous speech interactions and sentiment analysis.

| Model | Pricing (1M Tokens) |
|---|---|
| GPT-4o-Audio-Preview-Global | Text: Input: \$2.50 Text Cached Input: N/A Text Output: \$10 Audio: Input: \$100 Audio Cached Input: N/A Audio Output: \$200 |

### GPT-4o

GPT-4o is the most advanced multimodal model that’s faster and cheaper than GPT-4 Turbo with stronger vision capabilities. The model has 128K context and an October 2023 knowledge cutoff.

| Model | Pricing (1M Tokens) | Pricing with Batch API (1M Tokens) |
|---|---|---|
| GPT-4o-2024-08-06 | Global: Input: \$2.50 Cached Input: \$1.25 Output: \$10 | Global: Input: \$1.25 Output: \$5 |
|  | US/EU – Data Zones: Input: \$2.75 Cached Input: \$1.375 Output: \$11 | - |
|  | Regional: Input: \$2.75 Cached Input: \$1.375 Output: \$11 | - |

Plan with the [Pricing Calculator](https://gptforwork.com/tools/openai-chatgpt-api-pricing-calculator)

### GPT-4o mini

GPT-4o mini is the most cost-efficient small model, and has vision capabilities. The model has 128K context and an October 2023 knowledge cutoff.

| Model | Pricing (1M Tokens) | Pricing with Batch API (1M Tokens) |
|---|---|---|
| GPT-4o-mini | Global: Input: \$0.15 Cached Input: \$0.075 Output: \$0.60 | Global: Input: \$0.075 Output: \$0.30 |
|  | US/EU – Data Zones: Input: \$0.165 Cached Input: \$0.083 Output: \$0.66 | - |
|  | Regional: Input: \$0.165 Cached Input: \$0.083 Output: \$0.66 | - |

Plan with the [Pricing Calculator](https://gptforwork.com/tools/openai-chatgpt-api-pricing-calculator)

### Provisioned

You can allocate and manage throughput for deployments, ensuring predictable performance and stable capacity. You are charged an hourly rate per model regardless of usage, but you can also secure additional savings through monthly and annual reservations. Discover how to transition your regional deployments and provisioned reservations to global and data zones on this [Learn page](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/provisioned-get-started).

| Model | Min PTUs | PTU Hourly pricing | PTU Monthly Reservation Pricing | PTU Yearly Reservation Pricing |
|-------|----------|-------------------|--------------------------------|------------------------------|
| GPT-4o Global | 50 | \$1 | \$260 | \$2,652 |
| GPT-4o US/EU Data Zones | 50 | \$1.10 | \$260 | \$2,652 |
| GPT-4o Regional | 50 | \$2 | \$260 | \$2,652 |
| GPT-4o Mini Global | 25 | \$1 | \$260 | \$2,652 |
| GPT-4o Mini US/EU Data Zones | 25 | \$1.10 | \$260 | \$2,652 |
| GPT-4o Mini Regional | 25 | \$2 | \$260 | \$2,652 |

Plan with the [Pricing Calculator](https://gptforwork.com/tools/openai-chatgpt-api-pricing-calculator)

### Base models

| Models | Usage per 1,000 tokens |
|---|---|
| Babbage-002 | \$0.0004 |
| Davinci-002 | \$0.002 |

### Fine-tuning models

| Models | Training per 1,000 tokens | Hosting per hour | Input Usage per 1,000 tokens | Output Usage per 1,000 tokens | Cached Input per 1,000 tokens |
|---|---|---|---|---|---|
| Babbage-002 | N/A | N/A | N/A | N/A | N/A |
| Davinci-002 | N/A | N/A | N/A | N/A | N/A |
| GPT-3.5-Turbo (4K) | N/A | N/A | N/A | N/A | N/A |
| GPT-3.5-Turbo (16K) | N/A | N/A | N/A | N/A | N/A |
| GPT-4 (8K) | N/A | N/A | N/A | N/A | N/A |
| GPT-4o | N/A | N/A | N/A | N/A | N/A |
| GPT-4o-mini | N/A | N/A | N/A | \$0.000165 | N/A |
| GPT-4o-0806 | N/A | N/A | N/A | \$0.002063 | N/A |

### Assistants API

The Assistants API and its tools make it easy for developers to build AI Assistants in their applications.
The tokens used for the Assistants API are billed at the chosen language model's per token input/output rates used with each Assistant. Additionally, we charge the following fees for tool usage:

| Tool | Input |
|---|---|
| File Search | *\$0.10/GB of vector-storage per day (1 GB free) |
| Code Interpreter | **\$0.03/session**

**Notes:**

* **GB:** Refers to binary gigabytes, where 1 GB is 2^30 bytes.
* **Code Interpreter:** 
    * If your assistant calls Code Interpreter simultaneously in two different threads, this would create two Code Interpreter sessions (2 * \$0.03). 
    * Each session is active by default for one hour. 
    * You only pay this fee once if your user keeps giving instructions to Code Interpreter in the same thread for up to one hour.
    * Inference cost (input and output) varies based on the GPT model used with each Assistant. 
    * If your assistant calls Code Interpreter simultaneously in two different threads, this would create two Code Interpreter sessions (2 * \$0.03). 
    * Each session is active by default for one hour, which means that the price is for up to one hour of giving instructions to Code Interpreter in the same thread.

### Image models

| Models | Quality | Resolution | Price (per 100 images) |
|---|---|---|---|
| Dall-E-3 | Standard | 1024 * 1024 | \$4 |
| Dall-E-3 | Standard | 1024 * 1792, 1792 * 1024 | \$8 |
| Dall-E-3 | HD | 1024 * 1024 | \$8 |
| Dall-E-3 | HD | 1024 * 1792, 1792 * 1024 | \$12 |
| Dall-E-2 | Standard | 1024 * 1024 | \$2 |

### Embedding models

| Models | Per 1,000 tokens |
|---|---|
| Ada | \$0.0001 |
| text-embedding-3-large | \$0.00013 |
| text-embedding-3-small | \$0.00002 |

### Speech Models

Pricing is not available in the selected region

### Legacy Language Models

| Models | Context | Input (Per 1M Tokens) | Output (Per 1M Tokens) |
|---|---|---|---|
| GPT-3.5-Turbo-0301 | 4K | \$1.50 | \$2 |
| GPT-3.5-Turbo-0613 | 4K | \$1.50 | \$2 |
| GPT-3.5-Turbo-0613 | 16K | \$3 | \$4 |
| GPT-3.5-Turbo-1106 | 16K | \$1 | \$2 |
| GPT-3.5-Turbo-0125 | 16K | \$0.50 | \$1.50 |
| GPT-3.5-Turbo-Instruct | 4K | \$1.50 | \$2 |
| GPT-4-Turbo | 128K | \$10 | \$30 |
| GPT-4-Turbo-Vision | 128K | \$10 | \$30 |
| GPT-4 | 8K | \$30 | \$60 |
| GPT-4 | 32K | \$60 | \$120 |

---
---

## Standard Limits

### o1-preview & o1-mini global standard

| Model | Tier | Quota Limit in tokens per minute (TPM) | Requests per minute |
|---|---|---|---|
| o1-preview | Enterprise agreement | 30 M | 5 K |
| o1-mini | Enterprise agreement | 50 M | 5 K |
| o1-preview | Default | 3 M | 500 |
| o1-mini | Default | 5 M | 500 |

*M = million | K = thousand

### o1-preview & o1-mini standard

| Model | Tier | Quota Limit in tokens per minute (TPM) | Requests per minute |
|---|---|---|---|
| o1-preview | Enterprise agreement | 600 K | 100 |
| o1-mini | Enterprise agreement | 1 M | 100 |
| o1-preview | Default | 300 K | 50 |
| o1-mini | Default | 500 K | 50 |

*M = million | K = thousand

### gpt-4o & GPT-4 Turbo global standard

**Note:** gpt-4o and gpt-4o-mini, and gpt-4 (turbo-2024-04-09) have rate limit tiers with higher limits for certain customer types.

| Model | Tier | Quota Limit in tokens per minute (TPM) | Requests per minute |
|---|---|---|---|
| gpt-4o | Enterprise agreement | 30 M | 180 K |
| gpt-4o-mini | Enterprise agreement | 50 M | 300 K |
| gpt-4 (turbo-2024-04-09) | Enterprise agreement | 2 M | 12 K |
| gpt-4o | Default | 450 K | 2.7 K |
| gpt-4o-mini | Default | 2 M | 12 K |
| gpt-4 (turbo-2024-04-09) | Default | 450 K | 2.7 K |

*M = million | K = thousand

### gpt-4o data zone standard

| Model | Tier | Quota Limit in tokens per minute (TPM) | Requests per minute |
|---|---|---|---|
| gpt-4o | Enterprise agreement | 10 M | 60 K |
| gpt-4o-mini | Enterprise agreement | 20 M | 120 K |
| gpt-4o | Default | 300 K | 1.8 K |
| gpt-4o-mini | Default | 1 M | 6 K |

*M = million | K = thousand

### gpt-4o standard

| Model | Tier | Quota Limit in tokens per minute (TPM) | Requests per minute |
|---|---|---|---|
| gpt-4o | Enterprise agreement | 1 M | 6 K |
| gpt-4o-mini | Enterprise agreement | 2 M | 12 K |
| gpt-4o | Default | 150 K | 900 |
| gpt-4o-mini | Default | 450 K | 2.7 K |

*M = million | K = thousand


---
---

## Default Quotas and Limits

| Name | Limit | Value |
|---|---|---|
| Azure OpenAI resources per region per Azure subscription | Default | 30 |
| DALL-E 2 quota limits | Default | 2 concurrent requests |
| DALL-E 3 quota limits | Default | 2 capacity units (6 requests per minute) |
| Whisper quota limits | Default | 3 requests per minute |
| Maximum prompt tokens per request | Varies per model. For more information, see Azure OpenAI Service models |  |
| Max Standard deployments per resource | Default | 32 |
| Max fine-tuned model deployments | Default | 5 |
| Total number of training jobs per resource | Default | 100 |
| Max simultaneous running training jobs per resource | Default | 1 |
| Max training jobs queued | Default | 20 |
| Max Files per resource (fine-tuning) | Default | 50 |
| Total size of all files per resource (fine-tuning) | Default | 1 GB |
| Max training job time (job will fail if exceeded) | Default | 720 hours |
| Max training job size (tokens in training file) x (# of epochs) | Default | 2 Billion |
| Max size of all files per upload (Azure OpenAI on your data) | Default | 16 MB |
| Max number or inputs in array with /embeddings | Default | 2048 |
| Max number of /chat/completions messages | Default | 2048 |
| Max number of /chat/completions functions | Default | 128 |
| Max number of /chat completions tools | Default | 128 |
| Maximum number of Provisioned throughput units per deployment | Default | 100,000 |
| Max files per Assistant/thread | Default | 10,000 when using the API or Azure AI Foundry portal. In Azure OpenAI Studio the limit was 20. |
| Max file size for Assistants & fine-tuning | Default | 512 MB |
| Max size for all uploaded files for Assistants | Default | 100 GB |
| Assistants token limit | Default | 2,000,000 token limit |
| GPT-4o max images per request (# of images in the messages array/conversation history) | Default | 50 |
| GPT-4 vision-preview & GPT-4 turbo-2024-04-09 default max tokens | Default | 16 |
| Increase the max_tokens parameter value to avoid truncated responses. GPT-4o max tokens defaults to 4096. |  |  |
| Max number of custom headers in API requests | Default | 110 |
| Max number requests per minute | Default | 100 new connections per minute | 

**Note:** Current rate limits for real time audio (gpt-4o-realtime-preview) are defined as the number of new websocket connections per minute. For example, 100 requests per minute (RPM) means 100 new connections per minute.


---

### Global batch limits

| Global batch limits | Limit | Value |
|---|---|---|
| Max files per resource | Default | 500 |
| Max input file size | Default | 200 MB |
| Max requests per file | Default | 100,000 |

---

### Global batch quota

The table shows the batch quota limit. Quota values for global batch are represented in terms of enqueued tokens. When you submit a file for batch processing the number of tokens present in the file are counted. Until the batch job reaches a terminal state, those tokens will count against your total enqueued token limit.

| Model | Enterprise agreement | Default | Monthly credit card based subscriptions | MSDN subscriptions | Azure for Students, Free Trials |
|---|---|---|---|---|---|
| gpt-4o | 5 B | 200 M | 50 M | 90 K | N/A |
| gpt-4o-mini | 15 B | 1 B | 50 M | 90 K | N/A |
| gpt-4-turbo | 300 M | 80 M | 40 M | 90 K | N/A |
| gpt-4 | 150 M | 30 M | 5 M | 100 K | N/A |
| gpt-35-turbo | 10 B | 1 B | 100 M | 2 M | 50 K |

*B = Billion | M = Million | K = Thousand