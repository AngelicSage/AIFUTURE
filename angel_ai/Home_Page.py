import streamlit as st
import streamlit_authenticator as stauth
from image_logic import rand_img_set_size
# Set the app title and logo
st.set_page_config(page_title="Angel Math", layout="wide")

###Authentication###
import yaml
from yaml.loader import SafeLoader

with open('pages/config.YAML') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)
authenticator.login()
if st.session_state["authentication_status"]:
    st.write(f'Welcome *{st.session_state["name"]}*')
    authenticator.logout()
    
else:
    # Add a column for the buttons
    col4 = st.columns(2)

    # Create the 'Chat' button in the first column


    # Create the 'Lessons' button in the second column
    with col4[1]:
        register_button = st.button("Register")


    if register_button:
        st.switch_page('pages/register.py')
        

# Add the header and slogan and image
st.header("Angel Math")
st.image("images/OIG4.png", width=150)
st.subheader("Learn with Style")

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
col1, col2 = st.columns(2)

# Create the 'Chat' button in the first column

with col1:
    chat_button = st.button("Chat")

# Create the 'Lessons' button in the second column
with col2:
    lessons_button = st.button("Lessons")

if chat_button:
    st.switch_page('pages/Chat.py')

if lessons_button:
    st.switch_page('pages/Lessons.py')
    
