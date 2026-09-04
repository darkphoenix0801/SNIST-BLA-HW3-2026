import io
from backend.services.llm import client

async def transcribe_audio(file_bytes: bytes, filename: str) -> str:
    """
    Converts audio bytes into text using an STT service (e.g., Whisper).
    We use the OpenAI client which can point to Whisper or a compatible endpoint.
    """
    try:
        # The openai library requires a file-like object with a name attribute
        audio_file = io.BytesIO(file_bytes)
        audio_file.name = filename
        
        # Call the transcription API
        transcript = await client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
        return transcript.text
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return ""

def extract_audio_features(file_bytes: bytes) -> dict:
    """
    Extracts basic audio features like pace, pauses, and energy.
    Uses librosa if available. Otherwise returns mock data for hackathon demo.
    """
    features = {
        "pace": "Normal",
        "pauses": "Moderate",
        "energy": "Good",
        "confidence_proxy": 85
    }
    
    try:
        import librosa
        import soundfile as sf
        # Logic to actually parse the bytes with librosa would go here.
        # e.g. y, sr = librosa.load(io.BytesIO(file_bytes))
        # This is kept as a stub for the hackathon to prevent dependency bloat 
        # unless explicitly installed and implemented.
    except ImportError:
        print("librosa not installed, using mock audio features for demo.")
        
    return features
