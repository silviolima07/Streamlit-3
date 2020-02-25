# Core Pkgs
import streamlit as st 
from PIL import Image,ImageEnhance
import numpy as np 
import os, cv2

def main():
    """ A simple iris EDA App """

    st.title("Iris EDA App with streamlit")
    st.subheader("Streamlit is python server for web apps")

if __name__ == '__main__':
    main()

# path  
#path = r'/home/silvio/github/Streamlit-3/pessoas.jpeg'
  
# Reading an image in default mode 
#image = cv2.imread(path) 
  
# Window name in which image is displayed 
#window_name = 'image'
  
# Using cv2.imshow() method  
# Displaying the image  
#cv2.imshow(window_name, image)
