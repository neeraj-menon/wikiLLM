import os
from groq import Groq
from typing import List, Dict

class ChatHandler:
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.1-8b-instant"  # Using Mixtral for its strong performance and context handling
    
    def load_documentation(self, provider: str) -> str:
        """Load the documentation content for a given provider."""
        try:
            with open(os.path.join("Documentations", f"{provider}.md"), 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return f"Documentation for {provider} not found."

    def create_system_prompt(self, provider: str, doc_content: str) -> str:
        """Create a system prompt with the documentation content."""
        
        return f"""You are a helpful AI assistant with expertise in Language Model providers. 
                Your task is to answer questions about {provider} using the following documentation as context.
                Please provide accurate, concise answers based solely on this documentation:

                {doc_content}

                When answering:
                1. Only use information from the provided documentation.
                2. If the information isn't in the documentation, say so.
                3. Give your responses using markdown for better readability.
                4. Include specific details like prices, token limits, or features when relevant.
                5. If the information is in the form of a table, format it as a markdown table.
                6. Keep responses focused and to the point.
                """

    def get_chat_response(self, 
                         provider: str, 
                         user_message: str, 
                         chat_history: List[Dict[str, str]] = None) -> str:
        """Get a response from the LLM using the documentation as context."""
        # Load documentation
        doc_content = self.load_documentation(provider)
        
        # Create messages array with system prompt and chat history
        messages = [
            {"role": "system", "content": self.create_system_prompt(provider, doc_content)}
        ]
        
        # Add chat history if provided
        if chat_history:
            for msg in chat_history[-4:]:  # Include last 4 messages for context
                messages.append({"role": msg["role"], "content": msg["content"]})
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        try:
            # Get completion from Groq
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.1,  # Low temperature for more focused responses
                max_tokens=1024   # Limit response length
            )
            
            return completion.choices[0].message.content
            
        except Exception as e:
            return f"Error getting response: {str(e)}"
