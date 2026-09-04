from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.agents.orchestrator import InterviewOrchestrator
from backend.services.interview_service import generate_interview_question, evaluate_interview_answer
import backend.services.memory_service as memory_service

router = APIRouter(
    prefix="/interview",
    tags=["Agentic Interview Orchestrator"]
)

# Initialize the orchestrator with our SQLite memory service
orchestrator = InterviewOrchestrator(memory_service)

class AnswerSubmission(BaseModel):
    student_id: int
    question: str
    answer: str
    current_difficulty: str

@router.get("/next_question/{student_id}")
async def get_next_question(student_id: int):
    """
    Decides the next topic and difficulty, then generates a question.
    """
    # In a real app, you'd fetch the current session state from the DB. 
    # For this demo endpoint, we assume basic state if not provided.
    mock_session_state = {"last_answer_score": 50, "current_difficulty": "Basic"}
    
    try:
        decision = orchestrator.decide_next_action(student_id, mock_session_state)
        question_data = await generate_interview_question(decision["topic"], decision["difficulty"], decision["reason"])
        
        return {
            "decision_metadata": decision,
            "question": question_data.get("question")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/evaluate")
async def evaluate_answer(submission: AnswerSubmission):
    """
    Evaluates the student's text answer and updates memory (mocked memory update for now).
    """
    try:
        evaluation = await evaluate_interview_answer(submission.question, submission.answer)
        
        # Here you would typically save the evaluation score to `interview_sessions` in SQLite
        # memory_service.save_interview_result(submission.student_id, submission.current_difficulty, evaluation['score'])
        
        return {
            "status": "success",
            "evaluation": evaluation
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
