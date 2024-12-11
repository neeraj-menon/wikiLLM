import streamlit as st
import os
import sys
import tempfile
from PIL import Image
import io
import tiktoken
from chat_handler import ChatHandler

# Add the Groq modules directory to Python path
groq_modules_path = os.path.join("Documentations", "Groq")
sys.path.append(groq_modules_path)

# Import Groq modules
from Documentations.Groq.cost_calculator import calculate_processing_cost as calculate_groq_cost
from Documentations.Groq.image_token_calculator import calculate_image_tokens, validate_image_tokens
from Documentations.Groq.text_token_calculator import calculate_text_tokens

# Import Anthropic modules
from Documentations.Anthropic.token_calculator import calculate_anthropic_tokens

# Import OpenAI modules
from Documentations.OpenAI.token_calculator import calculate_openai_tokens, calculate_openai_cost

# Set page configuration
st.set_page_config(
    page_title="WikiLLM",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'chat_handler' not in st.session_state:
    # Initialize chat handler with Groq API key
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        api_key = st.secrets.get("GROQ_API_KEY", None)
    st.session_state.chat_handler = ChatHandler(api_key) if api_key else None

# Title and description
st.title("WikiLLM 📚")
st.markdown("### Your comprehensive guide to Language Model providers")

# Create tabs for Documentation, Tools, and Chat
tab1, tab2, tab3 = st.tabs(["Documentation", "Tools", "Chat"])

with tab1:
    # Dictionary mapping providers to their documentation files
    docs_path = "Documentations"
    providers = {
        "Groq": os.path.join(docs_path, "Groq.md"),
        "Anthropic": os.path.join(docs_path, "Anthropic.md"),
        "OpenAI": os.path.join(docs_path, "OpenAI.md"),
        "Mistral": os.path.join(docs_path, "Mistral.md"),
        "Gemini": os.path.join(docs_path, "Gemini.md"),
        "GitHub": os.path.join(docs_path, "GitHub.md"),
        "Azure OpenAI": os.path.join(docs_path, "Azure OpenAI.md")
    }

    # Create the dropdown menu
    selected_provider = st.selectbox(
        "Select LLM Provider",
        options=list(providers.keys()),
        index=None,
        placeholder="Choose a provider..."
    )

    # Display the selected documentation
    if selected_provider:
        try:
            with open(providers[selected_provider], 'r', encoding='utf-8') as file:
                content = file.read()
                if selected_provider == "Groq":
                    # Split content at the Pricing section
                    parts = content.split("# Pricing")
                    if len(parts) > 1:
                        st.markdown(parts[0] + "# Pricing")
                        # Display the image explicitly using Streamlit's image function
                        image_path = os.path.join(docs_path, "image01.png")
                        if os.path.exists(image_path):
                            st.image(image_path, caption="Groq Pricing")
                        # Display the rest of the content
                        st.markdown(parts[1])
                    else:
                        st.markdown(content)
                elif selected_provider == "Mistral":
                    # Split content at the Pricing section
                    parts = content.split("## Pricing")
                    if len(parts) > 1:
                        st.markdown(parts[0] + "## Pricing")
                        # Display the image explicitly using Streamlit's image function
                        image_path = os.path.join(docs_path, "image02.png")
                        if os.path.exists(image_path):
                            st.image(image_path, caption="Mistral Pricing")
                        # Display the rest of the content
                        st.markdown(parts[1])
                    else:
                        st.markdown(content)
                else:
                    st.markdown(content)
        except FileNotFoundError:
            st.error(f"Documentation file for {selected_provider} not found.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.info("Please select a provider to view their documentation.")

with tab2:
    st.header("LLM Tools")
    
    # Tool selection
    tool_type = st.radio(
        "Select Tool Type",
        ["Cost Calculator", "Text Token Calculator", "Image Token Calculator"]
    )

    if tool_type == "Cost Calculator":
        st.subheader("Cost Calculator")
        
        # Add a provider selection dropdown
        provider = st.selectbox(
            "Select Provider",
            [
                "OpenAI", 
                "Groq"
            ]
        )
        
        if provider == "OpenAI":
            # Add a model selection dropdown with all OpenAI models
            model_name = st.selectbox(
                "Select Model",
                [
                    # GPT-4o Models
                    "gpt-4o", 
                    "gpt-4o-2024-11-20", 
                    "gpt-4o-2024-08-06", 
                    "gpt-4o-2024-05-13",
                    "gpt-4o-audio-preview",
                    
                    # GPT-4o mini Models
                    "gpt-4o-mini", 
                    "gpt-4o-mini-2024-07-18",
                    
                    # o1 Models
                    "o1-preview", 
                    "o1-preview-2024-09-12",
                    "o1-mini", 
                    "o1-mini-2024-09-12",
                    
                    # Fine-Tuning Models
                    "gpt-4o-2024-08-06-ft",
                    "gpt-4o-mini-2024-07-18-ft",
                    "gpt-3.5-turbo-ft",
                    
                    # Realtime API Models
                    "gpt-4o-realtime-preview", 
                    "gpt-4o-realtime-preview-2024-10-01"
                ]
            )
            
            token_count = st.number_input("Enter number of tokens", min_value=1, value=1000)
            is_input = st.checkbox("Is this input tokens?", value=True)
            use_cached = st.checkbox("Use cached input pricing?", value=False)
            
            if st.button("Calculate Cost"):
                try:
                    cost_details = calculate_openai_cost(
                        token_count, 
                        model_name, 
                        is_input=is_input, 
                        use_cached=use_cached
                    )
                    
                    # Display detailed cost information
                    st.success(f"Model: {cost_details['model']}")
                    st.success(f"Token Count: {cost_details['token_count']}")
                    st.success(f"Token Type: {'Input' if cost_details['is_input'] else 'Output'}")
                    st.success(f"Cached Input: {cost_details['use_cached']}")
                    st.success(f"Price per Million Tokens: ${cost_details['price_per_million']:.4f}")
                    st.success(f"Total Cost: ${cost_details['total_cost']:.6f}")
                except Exception as e:
                    st.error(f"Error calculating cost: {str(e)}")
        
        elif provider == "Groq":
            # Add a model selection dropdown with Groq models
            model_name = st.selectbox(
                "Select Model",
                [
                    "llama-3.2-1b",
                    "llama-3.1-70b", 
                    "mixtral-8x7b", 
                    "llama-3.2-90b-vision"
                ]
            )
            
            token_count = st.number_input("Enter number of tokens", min_value=1, value=1000)
            is_input = st.checkbox("Is this input tokens?", value=True)
            
            if st.button("Calculate Cost"):
                try:
                    # Use Groq's calculate_processing_cost function
                    cost = calculate_groq_cost(
                        token_count, 
                        model_name, 
                        is_input=is_input
                    )
                    
                    # Display cost information
                    st.success(f"Model: {model_name}")
                    st.success(f"Token Count: {token_count}")
                    st.success(f"Token Type: {'Input' if is_input else 'Output'}")
                    st.success(f"Total Cost: ${cost:.6f}")
                except Exception as e:
                    st.error(f"Error calculating cost: {str(e)}")

    elif tool_type == "Text Token Calculator":
        st.subheader("Text Token Calculator")
        
        # Add a model selection dropdown
        model_type = st.selectbox(
            "Select Token Calculation Method",
            ["Groq/Transformers", "Anthropic", "OpenAI", "Tiktoken"]
        )
        
        text_input = st.text_area("Enter your text")
        
        if st.button("Calculate Tokens"):
            try:
                if model_type == "Groq/Transformers":
                    token_count = calculate_text_tokens(text_input)
                    st.success(f"Token count (Groq/Transformers): {token_count}")
                elif model_type == "Anthropic":
                    # Default to latest Sonnet model
                    anthropic_tokens = calculate_anthropic_tokens(text_input)
                    
                    # Display results
                    st.success(f"Model: {anthropic_tokens['model']}")
                    st.success(f"Token Count: {anthropic_tokens['token_count']}")
                    st.success(f"Within Limit: {anthropic_tokens['within_limit']}")
                    st.success(f"Remaining Tokens: {anthropic_tokens['remaining_tokens']}")
                elif model_type == "OpenAI":
                    # Default to GPT-4o model
                    openai_tokens = calculate_openai_tokens(text_input)
                    
                    # Display results
                    st.success(f"Model: {openai_tokens['model']}")
                    st.success(f"Token Count: {openai_tokens['token_count']}")
                    st.success(f"Within Limit: {openai_tokens['within_limit']}")
                    st.success(f"Remaining Tokens: {openai_tokens['remaining_tokens']}")
                    st.success(f"Encoding Used: {openai_tokens['encoding_used']}")
                else:
                    # Fallback to tiktoken
                    encoding = tiktoken.get_encoding("cl100k_base")
                    token_count = len(encoding.encode(text_input))
                    st.success(f"Token count (Tiktoken): {token_count}")
            except Exception as e:
                st.error(f"Error calculating tokens: {str(e)}")

    elif tool_type == "Image Token Calculator":
        st.subheader("Image Token Calculator")
        uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_file is not None:
            try:
                # Save the uploaded file temporarily
                temp_path = os.path.join(tempfile.gettempdir(), uploaded_file.name)
                with open(temp_path, 'wb') as temp_file:
                    temp_file.write(uploaded_file.getbuffer())
                
                # Validate and calculate image tokens
                image_tokens = validate_image_tokens(temp_path)
                
                if image_tokens is not None:
                    st.success(f"Estimated image tokens: {image_tokens['total_tokens']}")
                else:
                    st.error("Unable to calculate image tokens. Please check the image and try again.")
                
                # Optional: Display the uploaded image
                image = Image.open(temp_path)
                st.image(image, caption="Uploaded Image", use_column_width=True)
                
                # Clean up temporary file
                os.unlink(temp_path)
            except Exception as e:
                st.error(f"Error processing image: {str(e)}")

with tab3:
    st.header("Chat about LLM Documentation")
    
    if not st.session_state.chat_handler:
        st.error("Please set up your Groq API key to use the chat feature. You can set it as an environment variable 'GROQ_API_KEY' or in your Streamlit secrets.")
    else:
        # Provider selection for chat
        chat_provider = st.selectbox(
            "Select LLM Provider to discuss",
            ["Anthropic", "OpenAI", "Groq", "Mistral", "Gemini", "GitHub", "Azure OpenAI"],
            key="chat_provider"
        )
        
        # Clear chat button
        if st.button("Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()
        
        # Display chat history
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input(f"Ask me anything about {chat_provider}..."):
            # Add user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            
            # Get response from chat handler
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = st.session_state.chat_handler.get_chat_response(
                        chat_provider,
                        prompt,
                        st.session_state.chat_history[:-1]  # Exclude current message
                    )
                    st.markdown(response)
                    
            # Add assistant response to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
st.markdown("Created by Third Ray, Inc. 🚀")
