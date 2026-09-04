# Collaboration Strategy

## Team Constraints
**Hackathon:** Hack-the-Matrix, Technidhi 2026 — Track 01: AI Agents  
**Team Size:** 2 Developers  
**Time Limit:** Approximately 14 hours  

## Division of Labor

To maximize efficiency within the 14-hour constraint, the work should be split logically between the two developers.

### Developer A (AI & Backend Architecture)
**Focus:** Core agentic loop, ML integrations, and API design.
- **Featherless.ai Integration:** Managing API keys, setting up LLM prompts for question generation, evaluation, and resume parsing.
- **Backend API:** Building the FastAPI (or similar) endpoints.
- **Memory System:** Designing the state management to remember student answers and weaknesses.
- **Orchestrator Logic:** The decision-making loop (Thought → Action → Observation).

### Developer B (Frontend, Audio & Integration)
**Focus:** User experience, voice features, and system connection.
- **Frontend Development:** Building the UI for resume upload, roadmap display, and the chat/interview interface.
- **Voice Pipeline (If attempting):** Integrating Whisper STT and audio recording logic on the frontend.
- **ATS Analysis Display:** Formatting the ATS score and skill verification dashboard beautifully.
- **Integration Testing:** Ensuring the frontend properly sends and receives state from Developer A's APIs.

## Collaboration Best Practices
1. **API Contracts First:** Before coding, agree on the exact JSON structures for the API requests and responses. This allows both developers to work in parallel.
2. **Commit Often:** Follow the atomic commit strategy outlined in `implementationplan.md`. Use feature branches if needed.
3. **Mock Data:** Developer B should use hardcoded mock JSON responses initially so they aren't blocked waiting for Developer A's AI integrations to be perfect.
4. **Timeboxing:** If a feature (like advanced voice analysis) takes too long, fall back to the text-only interview and basic parsing to ensure a working demo.
