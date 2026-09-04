import json
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from utils.parser import parse_resume_file
from services.llm import analyze_resume_ats

router = APIRouter(
    prefix="/resume",
    tags=["Resume Intelligence"]
)

@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    target_company: str = Form("General")
):
    """
    Endpoint to upload a resume, extract its text, and analyze it with featherless.ai.
    """
    if not file.filename.lower().endswith(('.pdf', '.docx')):
        raise HTTPException(status_code=400, detail="Only PDF and DOCX are supported.")

    try:
        content = await file.read()
        extracted_text = parse_resume_file(content, file.filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse file: {str(e)}")

    if not extracted_text:
        raise HTTPException(status_code=400, detail="Could not extract any text from the file.")

    # Call featherless.ai to get skills and ATS score
    analysis_json_str = await analyze_resume_ats(extracted_text, target_company)
    
    try:
        analysis_data = json.loads(analysis_json_str)
    except json.JSONDecodeError:
        # Fallback if the model didn't return pure JSON
        analysis_data = {"raw_output": analysis_json_str}

    return {
        "filename": file.filename,
        "target_company": target_company,
        "analysis": analysis_data
    }
