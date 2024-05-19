import streamlit as st
import streamlit_authenticator as stauth

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

if st.session_state["authentication_status"]:
    st.write(f'Welcome *{st.session_state["name"]}*')
    authenticator.logout()
else:
    # Add a column for the buttons
    col3, col4 = st.columns(2)

    # Create the 'Chat' button in the first column

    with col3:
        login_button = st.button("Log In")

    # Create the 'Lessons' button in the second column
    with col4:
        register_button = st.button("Register")

    if login_button:
        st.switch_page('pages/login.py')

    if register_button:
        st.switch_page('pages/register.py')
   
#Resources
st.title('Resources')
st.header('Calculator')
st.write('https://www.desmos.com/scientific')
