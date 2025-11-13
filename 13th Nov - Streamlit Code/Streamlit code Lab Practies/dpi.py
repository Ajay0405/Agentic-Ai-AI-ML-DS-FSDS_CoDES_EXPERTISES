import streamlit as st 

from PIL import Image  # Import Image from Pillow
  fp = builtins.open(filename, "rb")
 img = Image.open("streamlit.png") # Open the image file
st.image(img, width=200) # Display the image with a specified width