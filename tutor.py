import streamlit as st
import random

def generate_mock_lesson(subject, difficulty):
    """
    Generate a mock lesson content
    """
    lessons = {
        "Mathematics": {
            "Beginner": "Introduction to Basic Algebra: Understanding Variables",
            "Intermediate": "Solving Quadratic Equations Using Different Methods",
            "Advanced": "Advanced Calculus: Derivatives and Their Applications"
        },
        "Science": {
            "Beginner": "Basic Concepts of Matter and Its States",
            "Intermediate": "Understanding Chemical Reactions",
            "Advanced": "Quantum Mechanics Fundamentals"
        },
        "Programming": {
            "Beginner": "Python Basics: Variables and Data Types",
            "Intermediate": "Object-Oriented Programming Concepts",
            "Advanced": "Advanced Algorithm Design and Optimization"
        }
    }
    return lessons.get(subject, {}).get(difficulty, "Lesson content not available")

def generate_mock_quiz(lesson_content):
    """
    Generate a mock quiz based on lesson content
    """
    return [
        {
            "question": f"What is the key concept in {lesson_content}?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "correct_answer": "Option A"
        },
        {
            "question": f"Another question related to {lesson_content}?",
            "options": ["Option X", "Option Y", "Option Z", "Option W"],
            "correct_answer": "Option Z"
        }
    ]

def app():
    """
    Tutor Session Page
    """
    st.title("AI Tutor Session")
    
    # Check authentication
    if 'authenticated' not in st.session_state or not st.session_state.get('authenticated'):
        st.warning("Please log in to access the tutor session.")
        return
    
    # Subject and difficulty selection
    st.sidebar.header("Session Configuration")
    subject = st.sidebar.selectbox(
        "Select Subject", 
        ["Mathematics", "Science", "Programming"]
    )
    difficulty = st.sidebar.selectbox(
        "Select Difficulty", 
        ["Beginner", "Intermediate", "Advanced"]
    )
    
    # Start lesson button
    if st.sidebar.button("Start Lesson"):
        # Generate lesson content
        lesson_content = generate_mock_lesson(subject, difficulty)
        st.session_state.current_lesson = lesson_content
        
        # Display lesson
        st.header(f"{subject} Lesson - {difficulty} Level")
        st.write(lesson_content)
        
        # Generate quiz
        st.session_state.current_quiz = generate_mock_quiz(lesson_content)
    
    # Quiz section
    if hasattr(st.session_state, 'current_quiz'):
        st.header("Quiz Time!")
        
        # Track quiz responses
        quiz_responses = {}
        
        for i, question in enumerate(st.session_state.current_quiz, 1):
            st.subheader(f"Question {i}")
            st.write(question['question'])
            
            # Quiz options
            quiz_responses[i] = st.radio(
                "Select your answer", 
                question['options'], 
                key=f"quiz_q{i}"
            )
        
        # Submit quiz
        if st.button("Submit Quiz"):
            # Mock scoring
            correct_answers = sum(
                quiz_responses[i+1] == q['correct_answer'] 
                for i, q in enumerate(st.session_state.current_quiz)
            )
            total_questions = len(st.session_state.current_quiz)
            score = (correct_answers / total_questions) * 100
            
            st.header("Quiz Results")
            st.metric("Score", f"{score:.2f}%")
            
            if score >= 80:
                st.success("Excellent job! You've mastered the key concepts.")
            elif score >= 60:
                st.warning("Good attempt. Review the lesson and try again.")
            else:
                st.error("You might want to review the lesson before retaking the quiz.")