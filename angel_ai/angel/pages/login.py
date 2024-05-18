import streamlit as st
import streamlit_authenticator as stauth
from image_logic import rand_nice_origin_size_gifs
from image_logic import rand_img_set_size
### Authentication ###

import yaml
from yaml.loader import SafeLoader

with open('/Users/whybless/Documents/ai/angel_ai/pages/config.YAML') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

#calling
authenticator.login()

#Authenticating users
if st.session_state["authentication_status"]:
    st.write(f'Welcome *{st.session_state["name"]}*')
    authenticator.logout()
    st.title('You Are Already Signed In')
    col5 = st.columns(2)
    with col5[1]:
        login_button = st.button("Home")
    if login_button:
        st.switch_page('/Users/whybless/Documents/ai/angel_ai/Home_Page.py')
    rand_nice_origin_size_gifs()
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
    col4 = st.columns(2)

    # Create the 'Register' button in the second column
    with col4[1]:
        register_button = st.button("Register")

    if register_button:
        st.switch_page('pages/register.py')
    rand_img_set_size(None, '/Users/whybless/Documents/ai/angel_ai/sus_gifs')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
    col4 = st.columns(2)

    # Create the 'Register' button in the second column
    with col4[1]:
        register_button = st.button("Register")

    if register_button:
        st.switch_page('pages/register.py')
    rand_img_set_size(None, '/Users/whybless/Documents/ai/angel_ai/sus_gifs')
    
# Updating the configuration file
with open('/Users/whybless/Documents/ai/angel_ai/pages/config.YAML', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)

