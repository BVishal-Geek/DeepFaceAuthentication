import cv2
import numpy as np
from PIL import Image
import streamlit as st
from scripts.capture_image import CaptureImage
from streamlit_navigation_bar import st_navbar
from config import TITLE, DESCRIPTION, VERSION

class app: 
    def __init__(self):
        self.title = TITLE
        self.description = DESCRIPTION
        self.version =  VERSION
    
    def home(self) -> None:
        '''home method displays the title, description, and version of the application.'''
        st.title(self.title)
        st.write(self.description)
        st.write("Version: ", self.version)
    
    def camera_streaming(self) -> None:
        '''camera_streaming method captures an image using Streamlit's built-in camera capture.'''
        enable: bool = st.checkbox("Enable Camera")
        try:
            '''Optional[np.ndarray] is used to handle NoneType returned by CaptureImage.live_stream()'''
            picture: Optional[np.ndarray] = CaptureImage.live_stream(disabled=not enable) 
            if picture:
                st.image(picture, caption="Captured Image", use_column_width=True)
        except Exception as e:
            st.write("Error: ", e)
        self.name = st.text_input("Enter your name")
        self.email = st.text_input("Enter your email")

    def navigation(self):
        '''navigation method displays the navigation bar and redirects to the selected option.'''
        options = st_navbar(["Home", "Store New User", "Authenticate User"])
        if options == "Home": 
            self.home()
            
        if options == "Store New User":
            self.camera_streaming()
        
    def run(self):
        '''run method is the entry point of the application.'''
        self.navigation()

if __name__ == "__main__":
    app = app()
    app.run()