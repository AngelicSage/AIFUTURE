#randomly going through dir for gif, keeping size 
import streamlit as st
import os
import random
import time


def rand_img_set_size(GIF_WIDTH, gif_directory):
    import streamlit as st
    import os
    import random
    import time

    # Function to get a list of all image files in the directory
    def get_image_files(directory):
        allowed_extensions = ['.png', '.jpg', '.jpeg', '.gif']  # Add other supported image formats if needed
        return [os.path.join(directory, file) for file in os.listdir(directory) if os.path.splitext(file)[1].lower() in allowed_extensions]

    # Function to display a random image or GIF with an optional size
    def display_random_image(width=None):
        image_files = get_image_files(gif_directory)
        if not image_files:
            st.error("No image files found in the directory.")
            return

        random_image = random.choice(image_files)
        st.image(random_image, width=width, use_column_width=False)


    # Display a random image or GIF initially
    display_random_image(GIF_WIDTH)










    
# If Not signed in: sus_gifs 

# Around video & corners of pages: stickers

# Quiz: math_memes

# Home: Learning memes (done)







# Already signed in: nice_gifs (done)
        
# random images w original sizes
def rand_nice_origin_size_gifs():
    # Directory containing GIFs
    gif_directory = 'nice_gifs'
    # Function to get a list of all GIF files in the directory
    def get_gif_files(directory):
        return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.gif')]

    # Function to display a random GIF
    def display_random_gif():
        gif_files = get_gif_files(gif_directory)
        if not gif_files:
            st.error("No GIF files found in the directory.")
            return

        random_gif = random.choice(gif_files)
        st.image(random_gif)

    # Function to continuously shuffle and display GIFs
    def display_gifs_in_loop():
        gif_files = get_gif_files(gif_directory)
        if not gif_files:
            st.error("No GIF files found in the directory.")
            return

        while True:
            random_gif = random.choice(gif_files)
            st.image(random_gif)
            time.sleep(5)  # Display each GIF for 5 seconds
            st.experimental_rerun()  # Rerun the app to display the next GIF

    # Display a random GIF initially
    display_random_gif()