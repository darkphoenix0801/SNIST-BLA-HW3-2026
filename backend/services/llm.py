import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

# Featherless.ai exposes an OpenAI-compatible endpoint
FEATHERLESS_API_KEY = os.getenv("FEATHERLESS_API_KEY")
FEATHERLESS_BASE_URL = os.getenv("FEATHERLESS_BASE_URL", "https://api.featherless.ai/v1")

# If you want to default to a specific model offered by featherless, specify it here.
DEFAULT_MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"

# We use the AsyncOpenAI client but point it to featherless
client = AsyncOpenAI(
    api_key=FEATHERLESS_API_KEY,
    base_url=FEATHERLESS_BASE_URL,
)

async def analyze_resume_ats(resume_text: str, target_company: str = "General") -> str:
    """
    Sends the resume text to featherless.ai to extract skills and provide an ATS score.
    """
    system_prompt = (
        "You are an expert ATS (Applicant Tracking System) and technical recruiter. "
        "Extract the candidate's skills as a JSON list, and provide an ATS score out of 100 "
        f"tailored to the target company/role: {target_company}. "
        "Return the output in a structured JSON format with 'skills' (list of strings) and 'ats_score' (integer), "
        "and 'recommendations' (string)."
    )

    try:
        response = await client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Here is the resume text:\n\n{resume_text}"}
            ],
            response_format={ "type": "json_object" }, # Depending on model support, this forces JSON
            temperature=0.2,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling featherless.ai: {e}")
        return '{"error": "Failed to analyze resume"}'
