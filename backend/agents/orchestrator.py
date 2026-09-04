import random

class InterviewOrchestrator:
    def __init__(self, memory_service):
        self.memory = memory_service

    def decide_next_action(self, student_id: int, current_session_state: dict) -> dict:
        """
        Observes the student's memory and current session, and decides the next topic and difficulty.
        """
        student_data = self.memory.get_student_memory(student_id)
        skills = student_data.get("skills", [])
        
        # If no skills are available, fallback
        if not skills:
            return {"topic": "General Programming", "difficulty": "Basic", "reason": "No specific skills found."}

        # Determine difficulty based on recent performance
        recent_score = current_session_state.get("last_answer_score", 50)
        current_difficulty = current_session_state.get("current_difficulty", "Basic")
        
        difficulties = ["Basic", "Intermediate", "Advanced", "Expert"]
        try:
            curr_idx = difficulties.index(current_difficulty)
        except ValueError:
            curr_idx = 0

        # Adapt difficulty
        if recent_score > 80 and curr_idx < len(difficulties) - 1:
            next_difficulty = difficulties[curr_idx + 1]
            reason = "Student performed well, increasing difficulty."
        elif recent_score < 40 and curr_idx > 0:
            next_difficulty = difficulties[curr_idx - 1]
            reason = "Student struggled, decreasing difficulty to rebuild confidence."
        else:
            next_difficulty = current_difficulty
            reason = "Maintaining difficulty based on steady performance."

        # Pick a topic (For demo purposes, we randomly select an unverified skill)
        # In a full production system, this would prioritize weaknesses or company requirements
        unverified_skills = [s['skill_name'] for s in skills if s['verification_level'] != 'Verified']
        
        if unverified_skills:
            next_topic = random.choice(unverified_skills)
        else:
            next_topic = random.choice([s['skill_name'] for s in skills])

        return {
            "topic": next_topic,
            "difficulty": next_difficulty,
            "reason": reason
        }
