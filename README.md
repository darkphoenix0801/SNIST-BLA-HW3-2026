# PADO — Placement Assessment and Development Orchestrator

**Hackathon Track:** AI Agents

PADO is a persistent-memory AI placement coach that verifies resume skills and conducts dynamic, agentic technical interviews. Powered by **featherless.ai**.

## Setup Instructions

1. **Clone the repository.**
2. **Set up the virtual environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -r frontend/requirements.txt
   ```
4. **Environment Variables:**
   - Copy `.env.example` to `.env`
   - Add your `FEATHERLESS_API_KEY` from featherless.ai

## Running the Application

You can run both the Backend and Frontend simultaneously by executing:
```bash
python run_pado.py
```

Alternatively, you can run them manually in separate terminals:
- **Backend:** `uvicorn backend.main:app --reload`
- **Frontend:** `streamlit run frontend/app.py`
