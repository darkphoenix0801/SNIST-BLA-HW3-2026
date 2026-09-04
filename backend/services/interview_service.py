import json
from backend.services.llm import client, DEFAULT_MODEL

async def generate_interview_question(topic: str, difficulty: str, context: str = "") -> dict:
    """
    Uses featherless.ai to generate an adaptive interview question.
    """
    system_prompt = (
        f"You are PADO, an expert technical interviewer. Generate ONE {difficulty}-level "
        f"interview question about {topic}. Do not provide the answer. "
        f"Context to consider: {context}. "
        "Return the output as JSON: {'question': 'your question text'}"
    )

    try:
        response = await client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[{"role": "system", "content": system_prompt}],
            response_format={"type": "json_object"},
            temperature=0.7,
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"Error generating question: {e}")
        return {"question": f"Tell me about your experience with {topic}."}

async def evaluate_interview_answer(question: str, answer: str) -> dict:
    """
    Uses featherless.ai to evaluate a student's answer.
    """
    system_prompt = (
        "You are an expert technical interviewer evaluating a candidate's answer. "
        f"Question asked: {question} \n"
        "Evaluate the candidate's answer out of 100. Identify any specific weaknesses. "
        "Return JSON format: {'score': int, 'feedback': 'str', 'weakness_tag': 'str'}"
    )

    try:
        response = await client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": answer}
            ],
            response_format={"type": "json_object"},
            temperature=0.2,
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"Error evaluating answer: {e}")
        return {"score": 50, "feedback": "Could not evaluate.", "weakness_tag": "unknown"}
