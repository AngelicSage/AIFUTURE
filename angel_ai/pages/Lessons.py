
import streamlit as st
import streamlit as st
import random

st.set_page_config(
    page_title="Angel AI",
    page_icon="👋",
)

st.title("Lesson 1")

video_file = open('/Users/whybless/Documents/ai/angel_ai/0513(1).mov', 'rb')
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
