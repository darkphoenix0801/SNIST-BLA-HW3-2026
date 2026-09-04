import subprocess
import sys
import time

def main():
    print("Starting PADO Backend (FastAPI)...")
    backend_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "backend.main:app", "--reload", "--port", "8000"]
    )
    
    # Wait a moment to ensure backend binds to the port
    time.sleep(2)
    
    print("Starting PADO Frontend (Streamlit)...")
    frontend_process = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "frontend/app.py"]
    )
    
    try:
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\nShutting down PADO...")
        backend_process.terminate()
        frontend_process.terminate()

if __name__ == "__main__":
    main()
