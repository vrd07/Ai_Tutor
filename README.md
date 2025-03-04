# AI Personal Tutor System

An AI-powered tutoring system built with FastAPI and Streamlit, leveraging LLM technologies (Mixtral and Deepseek via Ollama).

## Features

- Personalized learning experiences tailored to student level
- Automated lesson generation, quiz creation, and feedback
- Progress tracking and analytics
- Subject-specific teaching templates

## Technical Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Streamlit
- **Database**: SQLite
- **LLM**: Ollama (Mixtral and Deepseek models)
- **Authentication**: Auth0

## Getting Started

### Prerequisites

- Python 3.8+
- Ollama installed locally or accessible via API

### Installation

1. Clone the repository:

git clone https://github.com/yourusername/ai-tutor.git
cd ai-tutor

2. Set up virtual environments and install dependencies:

Backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Frontend
cd ../frontend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Configure environment variables:
- Create a `.env` file in the backend directory
- Add required variables (Auth0 credentials, etc.)

4. Start the services:
Backend
cd backend
uvicorn app.main:app --reload

Frontend
cd frontend
streamlit run app.py

## API Documentation

Access the API documentation at `http://localhost:8000/docs` when the backend is running.

## Architecture

[Include architecture diagram here]

## Development

[Include development guidelines here]

# AI Personal Tutor - User Guide

Welcome to your AI Personal Tutor! This guide will help you get the most out of your personalized learning experience.

## Getting Started

1. **Creating an Account**
   - Navigate to the Login/Register page
   - Click "Register" and enter your details
   - Verify your email address if required

2. **Setting Up Your Profile**
   - After logging in, go to the Profile page
   - Set your learning level (Beginner, Intermediate, Advanced)
   - Add subjects you're interested in

## Using the Tutor

1. **Starting a Learning Session**
   - Go to the Tutor Session page
   - Enter a topic you want to learn about
   - Select your knowledge level for this topic
   - Click "Begin Session"

2. **Interacting with the Tutor**
   - Type questions or responses in the text area
   - The AI tutor will provide explanations, examples, and guidance
   - Ask for clarification if needed

3. **Taking Quizzes**
   - Click "Generate Quiz" to test your understanding
   - Answer the questions provided
   - Submit your answers to receive feedback
   - Review explanations for any incorrect answers

4. **Tracking Your Progress**
   - Visit the Analytics page to view your learning journey
   - See scores across different subjects
   - Track improvement over time
   - Identify areas that need more focus

## Tips for Effective Learning

- Be specific about what you want to learn
- Ask follow-up questions to deepen understanding
- Use the quiz feature regularly to reinforce learning
- Review past sessions to consolidate knowledge

# User Acceptance Testing (UAT) Protocol

## Test Cases

### User Registration and Authentication
- [ ] User can register a new account
- [ ] User can log in with credentials
- [ ] User can log out
- [ ] User cannot access protected areas without logging in

### Student Profile Management
- [ ] User can create and update their profile
- [ ] User can set their learning level
- [ ] Profile information persists between sessions

### Learning Sessions
- [ ] User can start a new learning session on a specific topic
- [ ] AI tutor generates relevant lesson content
- [ ] User can interact with the tutor through text
- [ ] Conversation history is maintained during the session

### Quiz Generation and Assessment
- [ ] System can generate quizzes related to the lesson
- [ ] User can answer questions and submit responses
- [ ] System evaluates answers correctly
- [ ] User receives appropriate feedback

### Progress Tracking
- [ ] System records quiz scores
- [ ] User can view their historical performance
- [ ] Analytics show meaningful trends and insights

### System Performance
- [ ] Pages load within acceptable time (<3 seconds)
- [ ] AI responses are generated within reasonable time (<10 seconds)
- [ ] System handles concurrent users without degradation

## Feedback Collection

For each test case, please provide:
1. Pass/Fail status
2. Any issues encountered
3. Suggestions for improvement
4. Overall usability rating (1-5)

# AI Personal Tutor Launch Plan

## Pre-Launch Checklist

- [ ] All critical bugs resolved
- [ ] Security audit completed
- [ ] User documentation finalized
- [ ] Server provisioning completed
- [ ] Database backups configured
- [ ] API rate limiting tested
- [ ] Load testing completed

## Launch Day Schedule

### T-1 Day
- Finalize deployment scripts
- Prepare announcement materials
- Run final system tests
- Brief support team

### Launch Day
- 09:00 - Deploy backend to production server
- 10:00 - Deploy frontend to production server
- 11:00 - Conduct smoke test of all features
- 12:00 - Announce launch to initial user group
- 14:00 - Monitor system performance and user feedback
- 16:00 - Address any critical issues
- 18:00 - Send status report to stakeholders

## Post-Launch Monitoring

- Monitor server performance metrics
- Track API usage and response times
- Collect and analyze user feedback
- Prepare daily status reports for the first week

## Contingency Plans

### High Server Load
- Implement request queuing
- Scale up server resources
- Temporarily limit new user registrations

### Critical Bug Detection
- Deploy hotfix procedure
- Communicate timeline to users
- Consider rollback if severe

## Support Protocol

- Designate on-call personnel for the first 72 hours
- Establish priority levels for reported issues
- Define escalation procedures

## Troubleshooting

[Include common issues and solutions]

## Contact Support

[Include support contact information]