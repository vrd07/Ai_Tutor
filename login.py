import streamlit as st
from auth.streamlit_auth import auth0_login

def app():
    """
    Login and Registration page with Auth0
    """
    st.title("Login / Register")
    
    # Check if user is already authenticated
    if 'user' not in st.session_state:
        st.subheader("Login with Auth0")
        auth0_login()
    else:
        # User is logged in
        user = st.session_state.user
        st.success(f"Welcome, {user.get('name', 'User')}!")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("View Profile"):
                # Redirect to profile or show profile details
                st.write(f"Email: {user.get('email')}")
                st.image(user.get('picture'), width=150)
        
        with col2:
            if st.button("Logout"):
                # Clear the session
                del st.session_state.user
                st.experimental_rerun()