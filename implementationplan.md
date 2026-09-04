# PADO Implementation Plan

## Overview
This document outlines the step-by-step implementation plan for PADO (Placement Assessment and Development Orchestrator). 
Crucially, all LLM and AI models will be integrated using **featherless.ai** API keys and endpoints as requested.

## Phases & Commits Strategy

The project will be developed through structured phases, with atomic commits to maintain a clean history. We estimate around **15-20 total commits**.

### Phase 1: Environment Setup & Core Foundation (Estimated Commits: 3)
1. **Commit 1:** Initial repository setup, ignore files, and project skeleton.
2. **Commit 2:** Setup virtual environment, requirements.txt (FastAPI, pdfplumber, etc.).
3. **Commit 3:** Basic API routing and configuration structure (env variables for featherless.ai).

### Phase 2: Resume Intelligence & Parsing (Estimated Commits: 3)
4. **Commit 4:** Implement file upload endpoint (PDF/DOCX).
5. **Commit 5:** Implement `pdfplumber` and `python-docx` text extraction logic.
6. **Commit 6:** Integrate featherless.ai for ATS analysis and skills extraction from the parsed text.

### Phase 3: Memory & State Management (Estimated Commits: 3)
7. **Commit 7:** Setup database schema/models (e.g., SQLite/PostgreSQL) for user state.
8. **Commit 8:** Implement memory logic (Resume Truth/Skill Evidence Profile).
9. **Commit 9:** CRUD operations for storing test results and interview state.

### Phase 4: Agentic Interview Orchestrator (Estimated Commits: 4)
10. **Commit 10:** Create orchestrator logic for question selection (basic/intermediate/advanced).
11. **Commit 11:** Integrate featherless.ai models for dynamic question generation based on memory.
12. **Commit 12:** Implement answer evaluation logic (content scoring) via featherless.ai.
13. **Commit 13:** Implement text interview endpoints.

### Phase 5: Voice Pipeline (Optional/Advanced) (Estimated Commits: 3)
14. **Commit 14:** Audio recording upload and Whisper STT integration.
15. **Commit 15:** Audio feature extraction (librosa).
16. **Commit 16:** Multi-modal answer evaluation integration.

### Phase 6: Frontend & UI (Estimated Commits: 3)
17. **Commit 17:** Frontend setup (React/Next.js or simple HTML/JS) and routing.
18. **Commit 18:** Dashboard UI and resume upload component.
19. **Commit 19:** Chat/Interview UI component for text/voice interactions.
20. **Commit 20:** Final polish, UI bug fixes, and documentation.

## Guidelines for Committing
- Run `git add .` to stage files.
- Run `git commit -m "Phase X: Brief description of feature"`
- **Do not push all at once.** Push after each phase: `git push origin main`.
