import streamlit as st
import requests

def render_chat():
    st.markdown("### 🎙️ Adaptive Mock Interview")
    st.write("The Agentic Orchestrator will dynamically adjust question difficulty based on your performance.")
    
    student_id = st.number_input("Enter Student ID (e.g. 1)", min_value=1, value=1)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Get Next Question"):
            with st.spinner("Orchestrator is thinking..."):
                try:
                    res = requests.get(f"http://127.0.0.1:8000/interview/next_question/{student_id}")
                    if res.status_code == 200:
                        data = res.json()
                        st.session_state['current_q'] = data.get('question')
                        st.session_state['current_diff'] = data['decision_metadata']['difficulty']
                        st.success(f"**Topic:** {data['decision_metadata']['topic']} | **Difficulty:** {data['decision_metadata']['difficulty']}")
                        st.info(f"**Reason:** {data['decision_metadata']['reason']}")
                    else:
                        st.error(f"Error {res.status_code}: {res.text}")
                except Exception as e:
                    st.error(f"Backend error: {e}")

    # Display question if one exists in state
    if 'current_q' in st.session_state:
        st.markdown(f"#### Question:\n{st.session_state['current_q']}")
        
        answer = st.text_area("Your Answer:")
        if st.button("Submit Answer"):
            payload = {
                "student_id": student_id,
                "question": st.session_state['current_q'],
                "answer": answer,
                "current_difficulty": st.session_state['current_diff']
            }
            with st.spinner("Evaluating answer with featherless.ai..."):
                try:
                    eval_res = requests.post("http://127.0.0.1:8000/interview/evaluate", json=payload)
                    st.json(eval_res.json())
                except Exception as e:
                    st.error(f"Backend error: {e}")
