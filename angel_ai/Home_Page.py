import subprocess
import sys


import os
os.system('pip install pyyaml')
import os
os.system('pip install yaml')
import streamlit as st
import streamlit_authenticator as stauth
from image_logic import rand_img_set_size
import yaml
from yaml.loader import SafeLoader

# Set the app title and logo
st.set_page_config(page_title="Angel Math", layout="wide")

# Load the configuration file for authentication
with open('pages/config.YAML') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize the authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

# Login logic
authenticator.login()
if st.session_state["authentication_status"]:
    st.write(f'Welcome *{st.session_state["name"]}*')
    authenticator.logout()

else:
    # Create a column for the register button
    col1, col2 = st.columns([1, 3])  # Adjust the ratio to position the button on the left
    with col1:
        register_button = st.button("Register")

    if register_button:
        st.switch_page('pages/register.py')

# Add the header and slogan and image
st.title("🤯Angel Math🫣")
st.image("images/OIG4.png", width=150)
st.subheader("😎Learn with Style😎")

# Create the 'About website' section
with st.expander("About Website"):
    st.write("""This is an app that makes learning fun! Rather than watching a boring math lesson, get taught by your favorite influencers!""")

# Add the disclaimer
st.warning("Disclaimer: These AI voices are not of the real people. AI technology is used to mimic these voices.")

# Create columns
col6, col7 = st.columns(2)

# Display images side by side
with col6:
    rand_img_set_size(225, 'learning_memes')
with col7:
    rand_img_set_size(225, 'learning_memes')

# Add a column for the buttons
col3, col4 = st.columns(2)

# Create the 'Chat' button in the first column
with col3:
    chat_button = st.button("Chat")

# Create the 'Lessons' button in the second column
with col4:
    lessons_button = st.button("Lessons")

if chat_button:
    st.switch_page('pages/Chat.py')

if lessons_button:
    st.switch_page('pages/Lessons.py')
