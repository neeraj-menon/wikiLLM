# GitHub

### Overview
GitHub is a web-based platform for version control and code collaboration. It provides features such as code repositories, issue tracking, pull requests, and code review. GitHub is widely used by developers and open-source contributors to manage their projects and collaborate with others.

### Rate Limit (Free API)

| Rate Limit Tier | Requests per minute | Requests per day | Tokens per request | Concurrent requests |
|-----------------|-------------------:|----------------:|------------------:|-------------------:|
| Low (Free and Copilot Individual)	| 15 | 150 | 8000 in, 4000 out | 5 |
| Low (Copilot Business)| 15 | 300 | 8000 in, 4000 out | 5 |
| Low (Copilot Enterprise) | 15 | 450 | 8000 in, 4000 out | 5 |
| High (Free and Copilot Individual)| 10 | 50 | 8000 in, 4000 out | 2 |
| High (Copilot Business)| 10 | 100 | 8000 in, 4000 out | 2 |
| High (Copilot Enterprise) | 15 | 150 | 16000 in, 8000 out | 4 |
| Embedding (Free and Copilot Individual)| 15 | 150 | 64000 | 5 |
| Embedding (Copilot Business)| 15 | 300 | 64000 | 5 |
| Embedding (Copilot Enterprise) | 15 | 450 | 64000 | 5 |
| Azure OpenAI o1-preview (Free and Copilot Individual)| 1 | 2 | 4000 in, 4000 out | 1 |
| Azure OpenAI o1-preview (Copilot Business)| 2 | 8 | 4000 in, 4000 out | 1 |
| Azure OpenAI o1-preview (Copilot Enterprise) | 2 | 12 | 4000 in, 8000 out | 1 |
| Azure OpenAI o1-mini (Free and Copilot Individual)| 2 | 3 | 4000 in, 4000 out | 1 |
| Azure OpenAI o1-mini (Copilot Business)| 3 | 12 | 4000 in, 4000 out | 1 |
| Azure OpenAI o1-mini (Copilot Enterprise) | 3 | 20 | 4000 in, 4000 out | 1 |


---
---

### Available Models

| Model | Description | Tier | Limits |
|---|---|---|---|
| OpenAI GPT-4o | OpenAI's most advanced multimodal model in the GPT-4 family. Can handle both text and image inputs. | High | Large Language Model (LLM) |
| OpenAI GPT-4o mini | An affordable, efficient AI solution for diverse text and image tasks. | Low | Large Language Model (LLM) |
| OpenAI o1-mini | Smaller, faster, and 80% cheaper than o1-preview, performs well at code generation and small context operations. | Custom | Large Language Model (LLM) |
| OpenAI o1-preview | Focused on advanced reasoning and solving complex problems, including math and science tasks. Ideal for applications that require deep contextual understanding and agentic workflows. | Custom | Large Language Model (LLM) |
| OpenAI Text Embedding 3 (large) | Text-embedding-3 series models are the latest and most capable embedding model from OpenAI. | Embeddings | Embedding Model | 
| OpenAI Text Embedding 3 (small) | Text-embedding-3 series models are the latest and most capable embedding model from OpenAI. | Embeddings | Embedding Model | 
| Phi-3.5-MoE instruct (128k) | A new mixture of experts model | Low | Large Language Model (LLM) |
| Phi-3.5-mini instruct (128k) | Refresh of Phi-3-mini model. | Low | Large Language Model (LLM) |
| Phi-3.5-vision instruct (128k) | Refresh of Phi-3-vision model. | Low | Large Language Model (LLM) |
| Phi-3-medium instruct (128k) | Same Phi-3-medium model, but with a larger context size for RAG or few shot prompting. | Low | Large Language Model (LLM) |
| Phi-3-medium instruct (4k) | A 14B parameters model, proves better quality than Phi-3-mini, with a focus on high-quality, reasoning-dense data. | Low | Large Language Model (LLM) |
| Phi-3-mini instruct (128k) | Same Phi-3-mini model, but with a larger context size for RAG or few shot prompting. | Low | Large Language Model (LLM) |
| Phi-3-mini instruct (4k) | Tiniest member of the Phi-3 family. Optimized for both quality and low latency. | Low | Large Language Model (LLM) |
| Phi-3-small instruct (128k) | Same Phi-3-small model, but with a larger context size for RAG or few shot prompting. | Low | Large Language Model (LLM) |
| Phi-3-small instruct (8k) | A 7B parameters model, proves better quality than Phi-3-mini, with a focus on high-quality, reasoning-dense data. | Low | Large Language Model (LLM) |
| AI21 Jamba 1.5 Large | A 398B parameters (94B active) multilingual model, offering a 256K long context window, function calling, structured output, and grounded generation. | High | Large Language Model (LLM) |
| AI21 Jamba 1.5 Mini | A 52B parameters (12B active) multilingual model, offering a 256K long context window, function calling, structured output, and grounded generation. | Low | Large Language Model (LLM) |
| Cohere Command R | Command R is a scalable generative model targeting RAG and Tool Use to enable production-scale AI for enterprise. | Low | Large Language Model (LLM) |
| Cohere Command R 08-2024 | Command R is a scalable generative model targeting RAG and Tool Use to enable production-scale AI for enterprise. | Low | Large Language Model (LLM) |
| Cohere Command R+ | Command R+ is a state-of-the-art RAG-optimized model designed to tackle enterprise-grade workloads. | High | Large Language Model (LLM) |
| Cohere Command R+ 08-2024 | Command R+ is a state-of-the-art RAG-optimized model designed to tackle enterprise-grade workloads. | High | Large Language Model (LLM) |
| Cohere Embed v3 English | Cohere Embed English is the market's leading text representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. | Embeddings | Embedding Model |
| Cohere Embed v3 Multilingual | Cohere Embed Multilingual is the market's leading text representation model used for semantic search, retrieval-augmented generation (RAG), classification, and clustering. | Embeddings | Embedding Model |
| Llama-3.2-11B-Vision-Instruct | Excels in image reasoning capabilities on high-res images for visual understanding apps. | Low | Vision Model |
| Llama-3.2-90B-Vision-Instruct | Advanced image reasoning capabilities for visual understanding agentic apps. | High | Vision Model |
| Meta-Llama-3.1-405B-Instruct | The Llama 3.1 instruction tuned text only models are optimized for multilingual dialogue use cases and outperform many of the available open source and closed chat models on common industry benchmarks. | High | Large Language Model (LLM) |
| Meta-Llama-3.1-70B-Instruct | The Llama 3.1 instruction tuned text only models are optimized for multilingual dialogue use cases and outperform many of the available open source and closed chat models on common industry benchmarks. | High | Large Language Model (LLM) |
| Meta-Llama-3.1-8B-Instruct | The Llama 3.1 instruction tuned text only models are optimized for multilingual dialogue use cases and outperform many of the available open source and closed chat models on common industry benchmarks. | Low | Large Language Model (LLM) |
| Meta-Llama-3-70B-Instruct | A powerful 70-billion parameter model excelling in reasoning, coding, and broad language applications. | High | Large Language Model (LLM) |
| Meta-Llama-3-8B-Instruct | A versatile 8-billion parameter model optimized for dialogue and text generation tasks. | Low | Large Language Model (LLM) |
| Ministral 3B | Ministral 3B is a state-of-the-art Small Language Model (SLM) optimized for edge computing and on-device applications. As it is designed for low-latency and compute-efficient inference, it it also the perfect model for standard GenAI applications that have | Low | Small Language Model (SLM) |
| Mistral Nemo | Mistral Nemo is a cutting-edge Language Model (LLM) boasting state-of-the-art reasoning, world knowledge, and coding capabilities within its size category. | Low | Large Language Model (LLM) |
| Mistral Large | Mistral's flagship model that's ideal for complex tasks that require large reasoning capabilities or are highly specialized (Synthetic Text Generation, Code Generation, RAG, or Agents). | High | Large Language Model (LLM) |
| Mistral Large (2407) | Mistral Large (2407) is an advanced Large Language Model (LLM) with state-of-the-art reasoning, knowledge and coding capabilities. | High | Large Language Model (LLM) |
| Mistral Small | Mistral Small can be used on any language-based task that requires high efficiency and low latency. | Low | Small Language Model (SLM) |
| JAIS 30b Chat | JAIS 30b Chat is an auto-regressive bilingual LLM for Arabic & English with state-of-the-art capabilities in Arabic. | Low | Large Language Model (LLM) |
