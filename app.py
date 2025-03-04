import streamlit as st
from multipage import MultiPage
from pages import home, login, tutor, analytics, profile

def check_authentication(app_func):
    """
    Decorator to check authentication before rendering a page
    """
    def wrapper():
        if 'user' not in st.session_state:
            st.warning("Please log in to access this page.")
            login.app()
        else:
            app_func()
    return wrapper

st.set_page_config(page_title="AI Personal Tutor", layout="wide")

# Initialize the multi-page app
app = MultiPage()

# Add pages with authentication check for protected routes
app.add_page("Home", home.app)
app.add_page("Login/Register", login.app)

# Protected routes
app.add_page("Tutor Session", check_authentication(tutor.app))
app.add_page("Analytics", check_authentication(analytics.app))
app.add_page("Profile", check_authentication(profile.app))

# Main app
def main():
    st.sidebar.title("Navigation")
    
    # Run the app
    app.run()

if __name__ == "__main__":
    main()