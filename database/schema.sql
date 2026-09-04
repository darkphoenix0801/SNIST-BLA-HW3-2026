-- schema.sql

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    target_company TEXT,
    ats_score INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS skills_evidence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    skill_name TEXT,
    claimed BOOLEAN DEFAULT 1,
    verification_level TEXT DEFAULT 'Not Tested',
    confidence INTEGER DEFAULT 0,
    evidence_count INTEGER DEFAULT 0,
    FOREIGN KEY(student_id) REFERENCES students(id)
);

CREATE TABLE IF NOT EXISTS interview_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    topic TEXT,
    difficulty TEXT,
    question_count INTEGER,
    overall_score INTEGER,
    weaknesses TEXT, -- Stored as comma-separated or JSON
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(student_id) REFERENCES students(id)
);
