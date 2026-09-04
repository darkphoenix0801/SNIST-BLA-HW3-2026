import streamlit as st
import sys
import os

# Ensure the parent directory is in path so we can import components
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from components.chat_interface import render_chat

st.title("🤖 Adaptive Interview")
st.write("Experience the core of PADO's Agentic Orchestrator.")

# Render the interactive mock interview chat
render_chat()
