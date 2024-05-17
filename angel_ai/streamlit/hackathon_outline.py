import streamlit as st
import os

st.set_page_config(page_title="Angel AI", layout="wide")
st.image("""C:/Users/Brandom/Downloads/OIG4.png""", width=100)

st.header("Angel AI")
st.subheader("Learning under your favorite characters")

with st.expander("About Website"):
    st.write("""This is an app that makes learning fun! Rather than watching a boring math lesson, get taught by your favorite influencers!""")

# Add the disclaimer
st.warning("Disclaimer: These AI voices are not of the real people. AI technology is used to mimic these voices.")

# Add a column for the buttons
col1, col2 = st.columns(2)

# Create the 'Chat' button in the first column
with col1:
    if st.button("Chat"):
         st.title("Echo Bot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"Echo: {prompt}"

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

# Create the 'Lessons' button in the second column
with col2:
    if st.button("Lessons"):
        st.query_params(page="lessons")
        st.write("Redirecting to Lessons page...")
        st.sidebar.title('My Sidebar')

st.sidebar.write('Menu')
page_selection = st.sidebar.selectbox(label='', options=['Page 1', 'Page 2', 'Page 3'])
def page_1():
    st.write('Home')
def page_2():
    st.write('My Account')
def page_3():
    st.write('Settings')
if page_selection == 'Home':
    page_1()
elif page_selection == 'My Account':
    page_2()
elif page_selection == 'Settings':
    page_3()