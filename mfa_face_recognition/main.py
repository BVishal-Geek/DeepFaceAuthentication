import streamlit as st
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
    
    def capture_image(self):
        pass
    
    def store_new_user(self):
        st.title("Store New User")
        st.write("This is the store new user page")

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