import os
from fastapi import FastAPI
from dotenv import load_dotenv
from backend.routers import resume, interview

from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()

app = FastAPI(
    title="PADO - Placement Assessment and Development Orchestrator",
    description="Backend API for the PADO Agentic Placement Coach",
    version="1.0.0"
)

# Enable CORS for the Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Example featherless configuration check (for demonstration)
FEATHERLESS_API_KEY = os.getenv("FEATHERLESS_API_KEY")
FEATHERLESS_BASE_URL = os.getenv("FEATHERLESS_BASE_URL", "https://api.featherless.ai/v1")

@app.get("/")
async def root():
    return {
        "message": "PADO API is running.",
        "status": "active",
        "featherless_configured": bool(FEATHERLESS_API_KEY and FEATHERLESS_API_KEY != "your_featherless_api_key_here")
    }

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Include routers
app.include_router(resume.router)
app.include_router(interview.router)

