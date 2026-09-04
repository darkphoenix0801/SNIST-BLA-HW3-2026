import streamlit as st
import sys
import os

# Ensure the parent directory is in path so we can import components
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from components.resume_uploader import render_uploader

st.title("📊 PADO Dashboard")
st.write("Upload a student's resume to begin the verification and evidence loop.")

# Render the uploader component
render_uploader()
