import streamlit as st

def app():
    """
    Home page for the AI Personal Tutor application
    """
    st.title("Welcome to AI Personal Tutor")
    
    # Hero section
    st.header("Your Personalized Learning Companion")
    
    # Feature highlights
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🧠 Personalized Learning")
        st.write("Adaptive lessons tailored to your learning style and pace.")
    
    with col2:
        st.markdown("### 📊 Progress Tracking")
        st.write("Detailed analytics to monitor your learning journey.")
    
    with col3:
        st.markdown("### 🤖 AI-Powered Tutoring")
        st.write("Intelligent tutoring system with instant feedback.")
    
    # Call to action
    st.markdown("---")
    st.subheader("Ready to Start Learning?")
    
    # Motivational message
    st.write("""
    Our AI Personal Tutor adapts to your unique learning needs, 
    providing personalized guidance across multiple subjects.
    """)
    
    # Feature preview
    if st.button("Learn More"):
        with st.expander("About Our AI Tutor"):
            st.write("""
            ### How It Works
            1. Create a personalized profile
            2. Choose your learning subjects
            3. Start interactive AI-guided lessons
            4. Track your progress and improve
            
            Our AI uses advanced language models to:
            - Generate customized learning content
            - Create adaptive quizzes
            - Provide instant, detailed feedback
            """)