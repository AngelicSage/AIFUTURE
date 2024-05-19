import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from image_logic import rand_nice_origin_size_gifs
from image_logic import rand_img_set_size

# Load configuration from YAML file
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
authenticator.login()

# new user registration widget
if st.session_state["authentication_status"]:
    st.write(f'Welcome *{st.session_state["name"]}*')
    authenticator.logout()
    st.title('You Are Already Signed In')
    col5 = st.columns(2)
    with col5[1]:
        login_button = st.button("Home")
    if login_button:
        st.switch_page('Home_Page.py')
    rand_nice_origin_size_gifs()
    
else:
    try:
        rand_img_set_size(None, 'sus_gifs')
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
        col3 = st.columns(2)

        # Create the 'Chat' button in the first column

        with col3[1]:
            login_button = st.button("Log In")

        if login_button:
            st.switch_page('pages/login.py')
        if email_of_registered_user:
            st.success('User registered successfully')
            rand_nice_origin_size_gifs()
    except Exception as e:
        st.error(e)
        # Add a column for the buttons
        col3 = st.columns(2)

        # Create the 'Chat' button in the first column

        with col3[1]:
            login_button = st.button("Log In")

        if login_button:
            st.switch_page('pages/login.py')
        rand_img_set_size(None, 'sus_gifs')

# Update configuration file
with open('pages/config.YAML', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)


