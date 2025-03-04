# In frontend/pages/tutor.py
import streamlit as st
import requests
import json
from datetime import datetime

def tutor_page():
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.warning("Please login to access the tutoring system")
        return
    
    st.title("AI Personal Tutor Session")
    
    # Session setup
    if "current_session" not in st.session_state:
        st.subheader("Start a New Learning Session")
        topic = st.text_input("What would you like to learn about today?")
        levels = ["Beginner", "Intermediate", "Advanced"]
        level = st.selectbox("Select your knowledge level", levels)
        
        if st.button("Begin Session"):
            # Create a new session via API
            session_data = {"topic": topic, "level": level}
            # Placeholder for API call
            st.session_state.current_session = {
                "id": 1,  # This would come from the API response
                "topic": topic,
                "level": level,
                "messages": []
            }
            st.experimental_rerun()
    
    # Active session interface
    else:
        session = st.session_state.current_session
        st.subheader(f"Learning about: {session['topic']} ({session['level']} level)")
        
        # Display conversation history
        for msg in session["messages"]:
            if msg["is_from_student"]:
                st.text_area("You", msg["content"], height=100, disabled=True)
            else:
                st.text_area("AI Tutor", msg["content"], height=200, disabled=True)
        
        # User input
        user_input = st.text_area("Your message to the tutor", height=100)
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Send Message"):
                if user_input:
                    # Add user message to history
                    session["messages"].append({
                        "content": user_input,
                        "is_from_student": True,
                        "timestamp": datetime.now().isoformat()
                    })
                    
                    # Generate AI response - placeholder
                    ai_response = "This is a placeholder for the AI tutor's response."
                    
                    # Add AI message to history
                    session["messages"].append({
                        "content": ai_response,
                        "is_from_student": False,
                        "timestamp": datetime.now().isoformat()
                    })
                    
                    st.experimental_rerun()
        
        with col2:
            if st.button("Generate Quiz"):
                # Placeholder for quiz generation
                quiz = "This is a placeholder for a generated quiz."
                st.session_state.quiz = quiz
                
        with col3:
            if st.button("End Session"):
                # End session logic
                del st.session_state.current_session
                st.experimental_rerun()
        
        # Display quiz if available
        if "quiz" in st.session_state:
            st.subheader("Quiz")
            st.write(st.session_state.quiz)
            # Quiz interface would go here