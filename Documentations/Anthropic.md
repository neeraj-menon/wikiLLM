# Anthropic

### Overview
Anthropic is an AI safety and research company focused on developing reliable and interpretable AI systems. They are committed to advancing AI in a way that is safe and beneficial for humanity.

### Language Models Available on Anthropic with Context Windows

| Model ID | Owned By | Context Window | Notes |
|----------|----------|----------------|-------|
| claude-3-5-sonnet-20241022 | Anthropic | 200,000 | Latest and most capable mid-tier model |
| claude-3-opus-20240229 | Anthropic | 200,000 | Most capable model in the Claude 3 family |
| claude-3-sonnet-20240229 | Anthropic | 200,000 | Balanced model for performance and speed |
| claude-3-haiku-20240307 | Anthropic | 200,000 | Fastest and most compact model |

---
---
## Anthropic Rate Limits (Free Plan)

#### Chat Completions

| Model ID | Requests per minute | Tokens per minute |
|---|---|---|
| claude-3-opus-20240229 | 5 | 15,000 |
| claude-3-sonnet-20240229 | 5 | 15,000 |
| claude-3-haiku-20240307 | 5 | 15,000 |
| claude-2.1 | 5 | 15,000 |
| claude-2.0 | 5 | 15,000 |
| claude-instant-1.2 | 5 | 15,000 |

---
---
## Anthropic Pricing

#### Tier Wise Pricing
| Tier | Credit Purchase | Wait After First Purchase | Max Usage per Month | Monthly Invoicing |
|---|---|---|---|---|
| Tier 1 | $50 | days | $100 | N/A |
| Tier 2 | $40 | 7 days | $500 | N/A |
| Tier 3 | $200 | 7 days | $1,000 | N/A |
| Tier 4 | $400 | 14 days | $5,000 | N/A |

---

#### Tier 1 (*Rate Limit*):
| Model | Maximum requests per minute (RPM) | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
|---|---|---|---|
| Claude 3.5 Sonnet (2024-10-22) | 50 | 40,000 | 8,000 |
| Claude 3.5 Sonnet (2024-06-20) | 50 | 40,000 | 8,000 |
| Claude 3.5 Haiku | 50 | 50,000 | 10,000 |
| Claude 3 Opus | 50 | 20,000 | 4,000 |
| Claude 3 Sonnet | 50 | 40,000 | 8,000 |
| Claude 3 Haiku | 50 | 50,000 | 10,000 |

---
#### Tier 2 (*Rate Limit*):
| Model | Maximum requests per minute (RPM) | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
|---|---|---|---|
| Claude 3.5 Sonnet (2024-10-22) | 1,000 | 80,000 | 16,000 |
| Claude 3.5 Sonnet (2024-06-20) | 1,000 | 80,000 | 16,000 |
| Claude 3.5 Haiku | 1,000 | 100,000 | 20,000 |
| Claude 3 Opus | 1,000 | 40,000 | 8,000 |
| Claude 3 Sonnet | 1,000 | 80,000 | 16,000 |
| Claude 3 Haiku | 1,000 | 100,000 | 20,000 |

---
#### Tier 3 (*Rate Limit*):
| Model | Maximum requests per minute (RPM) | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
|---|---|---|---|
| Claude 3.5 Sonnet (2024-10-22) | 2,000 | 160,000 | 32,000 |
| Claude 3.5 Sonnet (2024-06-20) | 2,000 | 160,000 | 32,000 |
| Claude 3.5 Haiku | 2,000 | 200,000 | 40,000 |
| Claude 3 Opus | 2,000 | 80,000 | 16,000 |
| Claude 3 Sonnet | 2,000 | 160,000 | 32,000 |
| Claude 3 Haiku | 2,000 | 200,000 | 40,000 |

---
#### Tier 4 (*Rate Limit*):
| Model | Maximum requests per minute (RPM) | Maximum input tokens per minute (ITPM) | Maximum output tokens per minute (OTPM) |
|---|---|---|---|
| Claude 3.5 Sonnet (2024-10-22) | 4,000 | 400,000 | 80,000 |
| Claude 3.5 Sonnet (2024-06-20) | 4,000 | 400,000 | 80,000 |
| Claude 3.5 Haiku | 4,000 | 400,000 | 80,000 |
| Claude 3 Opus | 4,000 | 400,000 | 80,000 |
| Claude 3 Sonnet | 4,000 | 400,000 | 80,000 |
| Claude 3 Haiku | 4,000 | 400,000 | 80,000 |

2. **Pricing Structure**:
   - Separate pricing for input and output tokens
   - Higher prices for more capable models (e.g., Claude-3-opus)
   - Lower prices for smaller, faster models (e.g., Claude-3-haiku)
   - All prices in USD per 1 million tokens

3. **Key Features**:
   - High context windows (200K tokens for Claude 3)
   - Multimodal capabilities (images, code, text)
   - Advanced reasoning and analysis
   - Strong security and safety features

4. **Best Practices**:
   - Use Claude-3-haiku for quick, simple tasks
   - Use Claude-3-sonnet for balanced performance and cost
   - Use Claude-3-opus for complex tasks requiring deep analysis
   - Optimize prompts to reduce token usage
   - Implement proper error handling
   - Monitor token usage to control costs

---
---

# Custom Rate Limits used by Third Ray, Inc.

| Model | Requests per Minute | Input Tokens per Minute | Output Tokens per Minute |
|---|---|---|---|
| Claude 3.5 Sonnet (2024-10-22) | 4,000 | 400,000 | 80,000 |
| Claude 3.5 Sonnet (2024-06-20) | 4,000 | 400,000 | 80,000 |
| Claude 3.5 Haiku | 4,000 | 400,000 | 80,000 |
| Claude 3 Opus | 4,000 | 400,000 | 80,000 |
| Claude 3 Sonnet | 4,000 | 400,000 | 80,000 |
| Claude 3 Haiku | 4,000 | 400,000 | 80,000 |
