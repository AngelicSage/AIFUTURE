import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

st.title("ChatGPT-like clone with DeepSeekMath 7B")

# Load the model and tokenizer from Hugging Face
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-math-7b-instruct")
    
    # Check if the tokenizer has a pad token, if not set it to the eos token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-math-7b-instruct")
    return tokenizer, model

tokenizer, model = load_model()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare the input for the model
    input_text = "".join(
        [f"{message['role']}: {message['content']}\n" for message in st.session_state.messages]
    )
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=1000,
        do_sample=True,
        temperature=0.7,
        pad_token_id=tokenizer.pad_token_id
    )

    # Decode the model output and add it to the chat history
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)

# Clean up resources explicitly if needed
def cleanup_resources():
    # Any cleanup code here
    pass

cleanup_resources()
