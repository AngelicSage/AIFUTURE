import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
import toml

def update_secrets_toml(email, password, name, username):
    secrets_file_path = ".streamlit/secrets.toml"
    with open(secrets_file_path, "r") as f:
        secrets = toml.load(f)
    secrets["EMAIL"] = email
    secrets["PASS"] = password
    secrets["NAME"] = name  # Save the name to secrets.toml
    secrets["USERNAME"] = username  # Save the username to secrets.toml
    with open(secrets_file_path, "w") as f:
        toml.dump(secrets, f)

# App title
st.set_page_config(page_title="🤗💬 HugChat")

# Hugging Face Credentials and User Info
with st.sidebar:
    st.title('🤗💬 HugChat')
    if ('EMAIL' in st.secrets) and ('PASS' in st.secrets) and ('NAME' in st.secrets) and ('USERNAME' in st.secrets):
        st.success('HuggingFace Login credentials already provided!', icon='✅')
        hf_email = st.secrets['EMAIL']
        hf_pass = st.secrets['PASS']
        user_name = st.secrets['NAME']  # Retrieve the saved name
        user_username = st.secrets['USERNAME']  # Retrieve the saved username
    else:
        hf_email = st.text_input('Enter HuggingFace E-mail:', type='password')
        hf_pass = st.text_input('Enter HuggingFace Password:', type='password')
        st.warning("the next 2 are not from HuggingFace, but for this website")
        user_name = st.text_input('Enter Name:')
        user_username = st.text_input('Enter Username:')
        if not (hf_email and hf_pass and user_name and user_username):
            st.warning('Please enter all required information!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
            update_secrets_toml(hf_email, hf_pass, user_name, user_username)

    st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-an-llm-powered-chatbot-with-streamlit/)!')

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function for generating LLM response
def generate_response(prompt_input, email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # Create ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)

# User-provided prompt
if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt, hf_email, hf_pass)
            st.write(response)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
