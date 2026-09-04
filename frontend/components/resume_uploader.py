import streamlit as st
import requests

def render_uploader():
    st.markdown("### 📄 Resume Truth-Verification")
    st.write("Upload a resume to extract skills and compare against company requirements using featherless.ai.")
    
    uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])
    company = st.text_input("Target Company", "General (e.g. Google, Amazon)")
    
    if st.button("Analyze Resume & Extract Skills"):
        if uploaded_file is not None:
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
            data = {"target_company": company}
            
            with st.spinner("Analyzing resume through featherless.ai..."):
                try:
                    res = requests.post("http://127.0.0.1:8000/resume/upload", files=files, data=data)
                    if res.status_code == 200:
                        st.success("Analysis Complete!")
                        st.json(res.json())
                    else:
                        st.error(f"Error {res.status_code}: {res.text}")
                except Exception as e:
                    st.error(f"Backend connection error. Make sure FastAPI is running. Details: {e}")
        else:
            st.warning("Please upload a file first.")
