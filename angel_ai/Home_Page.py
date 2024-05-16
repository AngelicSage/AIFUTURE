import streamlit as st
# Set the app title and logo
st.set_page_config(page_title="Angel AI", layout="wide")

# Add the header and slogan
st.header("Angel AI")
st.subheader("Slogan")

# Create the 'About website' section
with st.expander("About Website"):
    st.write("""This is an app that makes learning fun! Rather than watching a boring math lesson, get taught by your favorite influencers!""")

# Add the disclaimer
st.warning("Disclaimer: These AI voices are not of the real people. AI technology is used to mimic these voices.")

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
    
