import streamlit as st
import streamlit_authenticator as stauth
from image_logic import rand_img_set_size
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
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')



col1, col2, col3 = st.columns(3)

# First column - GIF
with col1:
    rand_img_set_size(100, 'stickers')
    if st.session_state["authentication_status"]:
        st.write(f'Welcome *{st.session_state["name"]}*')
    else:
        register_button = st.button("Register", key="register_button")  # Manually assigned key
        if register_button:
            st.switch_page('pages/register.py')

# Second column - Video
with col2:
    st.title('Resources')

# Third column - GIF
with col3:
    rand_img_set_size(100, 'stickers')
    




#Resources

st.header('Calculator')
st.write('https://www.desmos.com/scientific')

st.header('Graphing Calculator')
st.write('https://www.desmos.com/calculator')
