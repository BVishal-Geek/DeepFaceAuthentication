import pytest
import streamlit as st
from mfa_face_recognition.main import app

def test_app():
    my_app = app()
    my_app.run()
    assert my_app is not None