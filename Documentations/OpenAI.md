# OpenAI


### Overview
OpenAI is a leading AI research and deployment company. Their mission is to ensure that artificial general intelligence (AGI) benefits all of humanity. OpenAI is known for its cutting-edge research and development of AI technologies.


### OpenAI Models Overview

#### GPT-4o
| Model | Context window | Max output tokens | Knowledge cutoff |
|---|---|---|---|
| gpt-4o | 128,000 tokens | 16,384 tokens | Oct 2023 |
| gpt-4o-2024-11-20 | 128,000 tokens | 16,384 tokens | Oct 2023 |
| gpt-4o-2024-08-06 | 128,000 tokens | 16,384 tokens | Oct 2023 |
| gpt-4o-2024-05-13 | 128,000 tokens | 4,096 tokens | Oct 2023 |
| chatgpt-4o-latest | 128,000 tokens | 16,384 tokens | Oct 2023 |

#### GPT-4o-mini
| Model | Context window | Max output tokens | Knowledge cutoff |
|---|---|---|---|
| gpt-4o-mini | 128,000 tokens | 16,384 tokens | Oct 2023 |
| gpt-4o-mini-2024-07-18 | 128,000 tokens | 16,384 tokens | Oct 2023 |
| GPT-4o Realtime + Audio | Beta |  |  |


#### GPT-4o Realtime + Audio *(Beta)*
| Model | Context window | Max output tokens | Knowledge cutoff |
|---|---|---|---|
| gpt-4o-realtime-preview | 128,000 tokens | 4,096 tokens | Oct 2023 |
| gpt-4o-realtime-preview-2024-10-01 | 128,000 tokens | 4,096 tokens | Oct 2023 |
| gpt-4o-audio-preview | 128,000 tokens | 16,384 tokens | Oct 2023 |
| gpt-4o-audio-preview-2024-10-01 | 128,000 tokens | 16,384 tokens | Oct 2023 |


#### o1-preview and o1-mini *(Beta)*
| Model | Context window | Max output tokens | Knowledge cutoff |
|---|---|---|---|
| o1-preview | 128,000 tokens | 32,768 tokens | Oct 2023 |
| o1-preview-2024-09-12 | 128,000 tokens | 32,768 tokens | Oct 2023 |
| o1-mini | 128,000 tokens | 65,536 tokens | Oct 2023 |
| o1-mini-2024-09-12 | 128,000 tokens | 65,536 tokens | Oct 2023 |


#### GPT-4 Turbo and GPT-4
| Model | Context window | Max output tokens | Knowledge cutoff |
|---|---|---|---|
| gpt-4-turbo | 128,000 tokens | 4,096 tokens | Dec 2023 |
| gpt-4-turbo-2024-04-09 | 128,000 tokens | 4,096 tokens | Dec 2023 |
| gpt-4-turbo-preview | 128,000 tokens | 4,096 tokens | Dec 2023 |
| gpt-4-0125-preview | 128,000 tokens | 4,096 tokens | Dec 2023 |
| gpt-4-1106-preview | 128,000 tokens | 4,096 tokens | Apr 2023 |
| gpt-4 | 8,192 tokens | 8,192 tokens | Sep 2021 |
| gpt-4-0613 | 8,192 tokens | 8,192 tokens | Sep 2021 |
| gpt-4-0314 | 8,192 tokens | 8,192 tokens | Sep 2021 |


#### GPT-3.5 Turbo
| Model | Context window | Max output tokens | Knowledge cutoff |
|---|---|---|---|
| gpt-3.5-turbo-0125 | 16,385 tokens | 4,096 tokens | Sep 2021 |
| gpt-3.5-turbo | 16,385 tokens | 4,096 tokens | Sep 2021 |
| gpt-3.5-turbo-1106 | 16,385 tokens | 4,096 tokens | Sep 2021 |
| gpt-3.5-turbo-instruct | 4,096 tokens | 4,096 tokens | Sep 2021 |



---
---


## Model Capabilities

### GPT-4o
- Most capable model in the GPT-4 series
- Advanced reasoning and complex problem-solving
- Superior coding and mathematical capabilities
- Enhanced creative writing and analysis
- Multilingual understanding and generation
- Consistent and reliable outputs
- Handles complex, multi-step instructions
- Excellent at technical and academic content
- Strong logical reasoning and deduction

### GPT-4o-mini
- Optimized for faster response times
- Balanced performance and efficiency
- Strong general knowledge capabilities
- Good at coding and technical tasks
- Cost-effective for medium complexity tasks
- Reliable for most general use cases
- Efficient context processing
- Suitable for production applications

### GPT-4o Realtime + Audio (Beta)
- Real-time conversation capabilities
- Audio processing and transcription
- Speech understanding and generation
- Low-latency responses
- Stream processing optimization
- Voice interaction support
- Multilingual audio processing
- Suitable for voice-based applications
- Real-time translation capabilities

### o1-preview and o1-mini (Beta)
#### o1-preview
- Next-generation architecture
- Enhanced reasoning capabilities
- Improved context understanding
- Better factual accuracy
- Advanced code generation
- Superior task planning
- Optimized for longer outputs
- Enhanced memory utilization
- Better at complex reasoning

#### o1-mini
- Lightweight next-gen model
- Fast inference times
- Efficient resource usage
- Good balance of capabilities
- Suitable for scaling
- Cost-effective processing
- Reliable for basic tasks
- Good at routine operations
- Optimized for production use

### GPT-4 Turbo
- Latest GPT-4 series model
- Up-to-date knowledge (Dec 2023)
- Advanced reasoning and creativity
- Complex task completion
- Code generation and analysis
- Research and analysis
- Multilingual proficiency
- JSON mode support
- Vision capabilities (vision variant)
- Parallel function calling
- Cost-effective for complex tasks

### GPT-4
- Robust and reliable model
- Complex instruction following
- Nuanced content creation
- Advanced coding capabilities
- Detailed analysis
- Research synthesis
- Strong logical reasoning
- Consistent performance
- Good for production use

### GPT-3.5 Turbo
- Fast and cost-effective
- Chat optimization
- Basic coding tasks
- Content generation
- Translation
- Summarization
- Quick response times
- Good for routine tasks
- Efficient token usage

---

## Usage Guidelines

### Best Practices
1. **Choose the Right Model**
   - Use GPT-4 Turbo for complex tasks requiring latest knowledge
   - Use GPT-4 for tasks needing high accuracy
   - Use GPT-3.5 Turbo for routine tasks and cost optimization

2. **Context Window Usage**
   - Consider token limits when designing prompts
   - Break large tasks into smaller chunks
   - Use efficient prompting techniques

3. **Cost Optimization**
   - Monitor token usage
   - Use GPT-3.5 Turbo for initial drafts
   - Implement caching where appropriate

4. **API Integration**
   - Implement proper error handling
   - Use appropriate timeouts
   - Monitor rate limits

---
---


## Model Limits with Cost

*Note:*
*Cached input pricing* charges users for accessing data stored in *cache*, offering lower costs and faster performance compared to retrieving data from its original source.

##### ***Key Points***
- *Caching* stores frequently used data in fast storage (e.g., RAM) to reduce latency and computation.
- Common models: flat fees, per-access fees, or size-based pricing.
- Used in *cloud services* (e.g., AWS, Google Cloud), *CDNs*, and *machine learning* to optimize performance.

##### ***Benefits***: 
Lower costs, faster access, and scalability.  
##### ***Challenges***: 
Cost predictability, cache expiry, and high initial access costs.


**GPT-4o Models**

| Model | Context Window | Max Output Tokens | Knowledge Cutoff | Input Token Price ($/M) | Output Token Price ($/M) | Cached Input Token Price ($/M) |
|---|---|---|---|---|---|---|
| gpt-4o | 128K | 16,384 | Oct 2023 | $2.50 | $10.00 | $1.25 |
| gpt-4o-2024-11-20 | 128K | 16,384 | Oct 2023 | $2.50 | $10.00 | $1.25 |
| gpt-4o-2024-08-06 | 128K | 16,384 | Oct 2023 | $2.50 | $10.00 | $1.25 |
| gpt-4o-audio-preview | 128K | 16,384 | Oct 2023 | $2.50 (text) | $10.00 (text) | - |
| |  |  |  | $100.00 (audio) | $200.00 (audio) | - |
| gpt-4o-audio-preview-2024-10-01 | 128K | 16,384 | Oct 2023 | $2.50 (text) | $10.00 (text) | - |
| |  |  |  | $100.00 (audio) | $200.00 (audio) | - |
| gpt-4o-2024-05-13 | 128K | 4,096 | Oct 2023 | $5.00 | $15.00 | $2.50 |

**GPT-4o mini Models**

| Model | Context Window | Max Output Tokens | Knowledge Cutoff | Input Token Price ($/M) | Output Token Price ($/M) | Cached Input Token Price ($/M) |
|---|---|---|---|---|---|---|
| gpt-4o-mini | 128K | 16,384 | Oct 2023 | $0.150 | $0.600 | $0.075 |
| gpt-4o-mini-2024-07-18 | 128K | 16,384 | Oct 2023 | $0.150 | $0.600 | $0.075 |

**OpenAI o1 Models**

| Model | Context Window | Max Output Tokens | Knowledge Cutoff | Input Token Price ($/M) | Output Token Price ($/M) | Cached Input Token Price ($/M) |
|---|---|---|---|---|---|---|
| o1-preview | 128K | 32,768 | Oct 2023 | $15.00 | $60.00 | $7.50 |
| o1-preview-2024-09-12 | 128K | 32,768 | Oct 2023 | $15.00 | $60.00 | $7.50 |
| o1-mini | 128K | 65,536 | Oct 2023 | $3.00 | $12.00 | $1.50 |
| o1-mini-2024-09-12 | 128K | 65,536 | Oct 2023 | $3.00 | $12.00 | $1.50 |

**Embedding Models**

| Model | Price ($/M tokens) | Price with Batch API ($/M tokens) |
|---|---|---|
| text-embedding-3-small | $0.020 | $0.010 |
| text-embedding-3-large | $0.130 | $0.065 |
| text-embedding-ada-002 | $0.100 | $0.050 |

**Fine-Tuning Models**

| Model | Input Token Price ($/M) | Output Token Price ($/M) | Cached Input Token Price ($/M) | Training Token Price ($/M) |
|---|---|---|---|---|
| gpt-4o-2024-08-06 | $3.750 | $15.000 | $1.875 | $25.000 |
| gpt-4o-mini-2024-07-18 | $0.300 | $1.200 | $0.150 | $3.000 |
| gpt-3.5-turbo | $3.000 | $6.000 | - | $8.000 |
| davinci-002 | $12.000 | $12.000 | - | $6.000 |
| babbage-002 | $1.600 | $1.600 | - | $0.400 |

**Realtime API**

| Model | Text Input Token Price ($/M) | Text Output Token Price ($/M) | Cached Text Input Token Price ($/M) | Audio Input Price ($/M) | Audio Output Price ($/M) | Cached Audio Input Price ($/M) |
|---|---|---|---|---|---|---|
| gpt-4o-realtime-preview | $5.00 | $20.00 | $2.50 | $100.00 | $200.00 | $20.00 |
| gpt-4o-realtime-preview-2024-10-01 | $5.00 | $20.00 | $2.50 | $100.00 | $200.00 | $20.00 |

**Image Models**

| Model | Quality | Resolution | Price ($/image) |
|---|---|---|---|
| DALL·E 3 | Standard | 1024x1024 | $0.040 |
| DALL·E 3 | Standard | 1024x1792, 1792x1024 | $0.080 |
| DALL·E 3 | HD | 1024x1024 | $0.080 |
| DALL·E 3 | HD | 1024x1792, 1792x1024 | $0.120 |
| DALL·E 2 |  | 1024x1024 | $0.020 |
| DALL·E 2 |  | 512x512 | $0.018 |
| DALL·E 2 |  | 256x256 | $0.016 |

**Audio Models**

| Model | Usage | Price |
|---|---|---|
| Whisper | per minute | $0.006 |
| TTS | per million characters | $15.000 |
| TTS HD | per million characters | $30.000 |


---
---

## Rate limits

How do these rate limits work?
------------------------------

Rate limits are measured in five ways: **RPM** (requests per minute), **RPD** (requests per day), **TPM** (tokens per minute), **TPD** (tokens per day), and **IPM** (images per minute). Rate limits can be hit across any of the options depending on what occurs first. For example, you might send 20 requests with only 100 tokens to the ChatCompletions endpoint and that would fill your limit (if your RPM was 20), even if you did not send 150k tokens (if your TPM limit was 150k) within those 20 requests.

[Batch API](/docs/api-reference/batch/create) queue limits are calculated based on the total number of input tokens queued for a given model. Tokens from pending batch jobs are counted against your queue limit. Once a batch job is completed, its tokens are no longer counted against that model's limit.

Other important things worth noting:

*   Rate limits are defined at the [organization level](/docs/guides/production-best-practices) and at the project level, not user level.
*   Rate limits vary by the [model](/docs/models) being used.
*   Limits are also placed on the total amount an organization can spend on the API each month. These are also known as "usage limits".
*   Some model families have shared rate limits. Any models listed under a "shared limit" in your [organizations limit page](https://platform.openai.com/settings/organization/limits) share a rate limit between them. For example, if the listed shared TPM is 3.5M, all calls to any model in the given "shared limit" list will count towards that 3.5M.

Usage tiers
-----------

You can view the rate and usage limits for your organization under the [limits](/settings/organization/limits) section of your account settings. As your usage of the OpenAI API and your spend on our API goes up, we automatically graduate you to the next usage tier. This usually results in an increase in rate limits across most models.

|Tier|Qualification|Usage limits|
|---|---|---|
|Free|User must be in an allowed geography|$100 / month|
|Tier 1|$5 paid|$100 / month|
|Tier 2|$50 paid and 7+ days since first successful payment|$500 / month|
|Tier 3|$100 paid and 7+ days since first successful payment|$1,000 / month|
|Tier 4|$250 paid and 14+ days since first successful payment|$5,000 / month|
|Tier 5|$1,000 paid and 30+ days since first successful payment|$200,000 / month|

Tier Wise Rate Limits per model.


#### Free tier rate limits

This is a high level summary and there are per-model exceptions to these limits (e.g. some legacy models or models with larger context windows have different rate limits). To view the exact rate limits per model for your account, visit the [limits](/settings/organization/limits) section of your account settings.

|Model|RPM|RPD|TPM|Batch Queue Limit|
|---|---|---|---|---|
|gpt-3.5-turbo|3|200|40,000|200,000|
|text-embedding-3-large|3,000|200|1,000,000|3,000,000|
|text-embedding-3-small|3,000|200|1,000,000|3,000,000|
|text-embedding-ada-002|3,000|200|1,000,000|3,000,000|
|omni-moderation-*|500|10,000|10,000|-|
|whisper-1|3|200|-|-|
|tts-1|3|200|-|-|
|dall-e-2|5 img/min|-|-|-|
|dall-e-3|1 img/min|-|-|-|


#### Tier 1 rate limits

|Model|RPM|RPD|TPM|Batch Queue Limit|
|:---|:---|:---|:---|:---|
|gpt-4o|500|30,000|90,000||
|gpt-4o-mini|500|10,000|200,000|2,000,000|
|gpt-4o-realtime-preview|100|100|20,000||
|o1-preview|500|30,000|90,000||
|o1-mini|500|10,000|200,000|2,000,000|
|gpt-4-turbo|500|30,000|90,000||
|gpt-4|500|10,000|10,000|100,000|
|gpt-3.5-turbo|3,500|10,000|200,000|2,000,000|
|omni-moderation-*|500|10,000|10,000||
|text-embedding-3-large|3,000|1,000,000|3,000,000||
|text-embedding-3-small|3,000|1,000,000|3,000,000||
|text-embedding-ada-002|3,000|1,000,000|3,000,000||
|whisper-1|1,500||||
|tts-1|1,500||||
|tts-1-hd|500||||
|dall-e-2|500 img/min||||
|dall-e-3|500 img/min||||


#### Tier 2 rate limits

| Model | RPM | TPM | Batch Queue Limit |
|---|---|---|---|
| gpt-4o | 5,000 | 450,000 | 1,350,000 |
| gpt-4o-mini | 5,000 | 2,000,000 | 20,000,000 |
| gpt-4o-realtime-preview | 200 | 40,000 | - |
| o1-preview | 5,000 | 450,000 | 1,350,000 |
| o1-mini | 5,000 | 2,000,000 | 20,000,000 |
| gpt-4-turbo | 5,000 | 450,000 | 1,350,000 |
| gpt-4 | 5,000 | 40,000 | 200,000 |
| gpt-3.5-turbo | 3,500 | 2,000,000 | 5,000,000 |
| omni-moderation-* | 500 | 20,000 | - |
| text-embedding-3-large | 5,000 | 1,000,000 | 20,000,000 |
| text-embedding-3-small | 5,000 | 1,000,000 | 20,000,000 |
| text-embedding-ada-002 | 5,000 | 1,000,000 | 20,000,000 |
| whisper-1 | 2,500 | - | - |
| tts-1 | 2,500 | - | - |
| tts-1-hd | 2,500 | - | - |
| dall-e-2 | 2,500 img/min | - | - |
| dall-e-3 | 2,500 img/min | - | - |


#### Tier 3 rate limits

| Model | RPM | TPM | Batch Queue Limit |
|---|---|---|---|
| gpt-4o | 5,000 | 800,000 | 50,000,000 |
| gpt-4o-mini | 5,000 | 4,000,000 | 40,000,000 |
| gpt-4o-realtime-preview | 5,000 | 400,000 | - |
| o1-preview | 5,000 | 800,000 | 50,000,000 |
| o1-mini | 5,000 | 4,000,000 | 40,000,000 |
| gpt-4-turbo | 5,000 | 600,000 | 40,000,000 |
| gpt-4 | 5,000 | 80,000 | 5,000,000 |
| gpt-3.5-turbo | 3,500 | 4,000,000 | 100,000,000 |
| omni-moderation-* | 1,000 | 50,000 | - |
| text-embedding-3-large | 5,000 | 5,000,000 | 100,000,000 |
| text-embedding-3-small | 5,000 | 5,000,000 | 100,000,000 |
| text-embedding-ada-002 | 5,000 | 5,000,000 | 100,000,000 |
| whisper-1 | 5,000 | - | - |
| tts-1 | 5,000 | - | - |
| tts-1-hd | 5,000 | - | - |
| dall-e-2 | 5,000 img/min | - | - |
| dall-e-3 | 5,000 img/min | - | - |


#### Tier 4 rate limits

|Model|RPM|TPM|Batch Queue Limit|
|:---|:---|:---|:---|
|gpt-4o|5,000|800,000|50,000,000|
|gpt-4o-mini|5,000|4,000,000|40,000,000|
|gpt-4o-realtime-preview|5,000|400,000||
|o1-preview|5,000|800,000|50,000,000|
|o1-mini|5,000|4,000,000|40,000,000|
|gpt-4-turbo|5,000|600,000|40,000,000|
|gpt-4|5,000|80,000|5,000,000|
|gpt-3.5-turbo|3,500|4,000,000|100,000,000|
|omni-moderation-*|1,000|50,000||
|text-embedding-3-large|5,000|5,000,000|100,000,000|
|text-embedding-3-small|5,000|5,000,000|100,000,000|
|text-embedding-ada-002|5,000|5,000,000|100,000,000|
|whisper-1|5,000||||
|tts-1|5,000||||
|tts-1-hd|5,000||||
|dall-e-2|5,000||||
|dall-e-3|5,000||||


#### Tier 5 rate limits

| Model | RPM | TPM | Batch Queue Limit |
|---|---|---|---|
| gpt-4o | 10,000 | 30,000,000 | 5,000,000,000 |
| gpt-4o-mini | 30,000 | 150,000,000 | 15,000,000,000 |
| gpt-4o-realtime-preview | 20,000 | 10,000,000 | - |
| o1-preview | 10,000 | 30,000,000 | 5,000,000,000 |
| o1-mini | 30,000 | 150,000,000 | 15,000,000,000 |
| gpt-4-turbo | 10,000 | 2,000,000 | 300,000,000 |
| gpt-4 | 10,000 | 1,000,000 | 150,000,000 |
| gpt-3.5-turbo | 10,000 | 50,000,000 | 10,000,000,000 |
| omni-moderation-* | 5,000 | 500,000 | - |
| text-embedding-3-large | 10,000 | 10,000,000 | 4,000,000,000 |
| text-embedding-3-small | 10,000 | 10,000,000 | 4,000,000,000 |
| text-embedding-ada-002 | 10,000 | 10,000,000 | 4,000,000,000 |
| whisper-1 | 10,000 | - | - |
| tts-1 | 10,000 | - | - |
| tts-1-hd | 10,000 | - | - |
| dall-e-2 | 10,000 img/min | - | - |
| dall-e-3 | 10,000 img/min | - | - |





### Rate limits in headers

In addition to seeing your rate limit on your [account page](/settings/organization/limits), you can also view important information about your rate limits such as the remaining requests, tokens, and other metadata in the headers of the HTTP response.

You can expect to see the following header fields:

|Field|Sample Value|Description|
|---|---|---|
|x-ratelimit-limit-requests|60|The maximum number of requests that are permitted before exhausting the rate limit.|
|x-ratelimit-limit-tokens|150000|The maximum number of tokens that are permitted before exhausting the rate limit.|
|x-ratelimit-remaining-requests|59|The remaining number of requests that are permitted before exhausting the rate limit.|
|x-ratelimit-remaining-tokens|149984|The remaining number of tokens that are permitted before exhausting the rate limit.|
|x-ratelimit-reset-requests|1s|The time until the rate limit (based on requests) resets to its initial state.|
|x-ratelimit-reset-tokens|6m0s|The time until the rate limit (based on tokens) resets to its initial state.|

---
---

# Additional Features

## Vision Capabilities
- Available in GPT-4 Vision Preview
- Supports image analysis and understanding
- Can process images up to 20MB
- Supports various image formats (PNG, JPEG, WEBP, GIF)

## JSON Mode
- Available in GPT-4 Turbo
- Ensures responses are valid JSON
- Useful for API integrations
- Reduces parsing errors

## Function Calling
- Supports parallel function calling
- Structured data extraction
- Tool and API integration
- Available in all models

## Reproducible Outputs
- Seed parameter for consistent outputs
- Available in GPT-4 Turbo
- Useful for testing and debugging

---

# Security and Safety

1. **Rate Limiting**
   - Implements per-minute and per-day limits
   - Prevents abuse and ensures fair usage
   - Automatic throttling on exceeding limits

2. **Content Filtering**
   - Built-in content moderation
   - Prevents harmful outputs
   - Customizable content policies

3. **API Authentication**
   - Secure API key management
   - Organization-level access control
   - Usage monitoring and logging
