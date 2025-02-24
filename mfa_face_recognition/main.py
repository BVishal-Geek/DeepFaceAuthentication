import streamlit as st
from PIL import Image
import numpy as np
import cv2
from streamlit_navigation_bar import st_navbar
from scripts.capture_image import *

class app: 
    def __init__(self):
        self.title = "Deep Face Authentication Using Face Recognition"
        self.description = "This is an application (0.1 version) for developing Multi-Factor Authentication (MFA) using face recognition."
        self.version = "0.1"
    
    def home(self):
        st.title(self.title)
        st.write(self.description)
        st.write("Version: ", self.version)
    
    def capture_image(self, disabled=None):
        st.title("Capture Image")

        # Streamlit's built-in camera capture
        captured_image = st.camera_input("Take a picture", disabled=disabled)

        if captured_image is not None:
            # Convert Streamlit image to OpenCV format
            image = Image.open(captured_image)
            image = np.array(image)  # Convert PIL Image to NumPy array

            # Convert RGB to BGR (OpenCV format)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            return image  # Return the processed image
        return None
    
    def store_new_user(self):
        st.title("Store New User")
        st.write("This is the store new user page")
        enable = st.checkbox("Enable Camera")
        picture = self.capture_image(disabled=not enable)
        if picture:
            st.image(picture, caption="Captured Image", use_column_width=True)
        self.name = st.text_input("Enter your name")
        self.email = st.text_input("Enter your email")
        

    def navigation(self):
        options = st_navbar(["Home", "Store New User", "Authenticate User"])
        if options == "Home": 
            self.home()
            
        if options == "Store New User":
            self.store_new_user()
        
    def run(self):
        self.navigation()

if __name__ == "__main__":
    app = app()
    app.run()