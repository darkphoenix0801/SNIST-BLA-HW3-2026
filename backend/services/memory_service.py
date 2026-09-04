import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database', 'pado.db')
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database', 'schema.sql')

def init_db():
    """Initializes the database using schema.sql if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def create_student(name: str, target_company: str, ats_score: int) -> int:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, target_company, ats_score) VALUES (?, ?, ?)",
        (name, target_company, ats_score)
    )
    student_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return student_id

def add_skills_evidence(student_id: int, skills: list):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for skill in skills:
        cursor.execute(
            "INSERT INTO skills_evidence (student_id, skill_name, claimed) VALUES (?, ?, 1)",
            (student_id, skill)
        )
    conn.commit()
    conn.close()

def get_student_memory(student_id: int) -> dict:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = dict(cursor.fetchone() or {})
    
    cursor.execute("SELECT * FROM skills_evidence WHERE student_id = ?", (student_id,))
    skills = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    
    return {
        "student": student,
        "skills": skills
    }
