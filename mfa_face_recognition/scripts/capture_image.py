from PIL import Image
import numpy as np
import cv2
import streamlit as st

class CaptureImage:
    '''live_stream method captures an image using Streamlit's built-in camera capture.'''
    @staticmethod
    def live_stream(disabled=None):
        st.title("Capture Image")

        # Streamlit's built-in camera capture
        captured_image = st.camera_input("Take a picture", disabled=disabled)
        if captured_image:
            # Convert Streamlit image to OpenCV format
            image = Image.open(captured_image)
            image = np.array(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            return image
        return None
    