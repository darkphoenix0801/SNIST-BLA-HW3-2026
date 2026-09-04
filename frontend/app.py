import streamlit as st

st.set_page_config(
    page_title="PADO | AI Placement Coach",
    page_icon="🎓",
    layout="wide"
)

# Inject custom CSS
try:
    with open("styles/main.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

st.title("Welcome to PADO 🚀")
st.markdown("### Placement Assessment and Development Orchestrator")

st.markdown("""
**Hackathon Demo: Track 01 - AI Agents**

PADO doesn't just test students — it verifies what they claim, remembers how they perform, and logically changes what happens next.

⬅️ **Use the sidebar to navigate to:**
1. **Dashboard:** Upload resumes and extract skills using featherless.ai.
2. **Interview:** Engage with the adaptive agentic orchestrator.
""")

st.info("Ensure the FastAPI backend is running on `http://127.0.0.1:8000` before starting.")
