import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title="Angel Math",
    page_icon="👋",
)

###Authentication###
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
   


import streamlit as st
from image_logic import rand_img_set_size  # Import the rand_img_set_size function


video_file = open('Appropriate_vid.mov', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.subheader('Productivity tip:')
st.write('Use split screen to reference the video while answering questions')

# Add a column for the buttons
col1, col2 = st.columns(2)

# Create the 'Chat' button in the first column
with col1:
    chat_button = st.button("Chat")

# Create the 'Lessons' button in the second column
with col2:
    quiz_button = st.button("Quiz")

if chat_button:
    st.switch_page('pages/Chat.py')

if quiz_button:
    st.switch_page('pages/Quiz.py')




