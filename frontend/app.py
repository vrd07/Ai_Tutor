import streamlit as st
from multipage import MultiPage
from pages import home, login, tutor, analytics, profile

st.set_page_config(page_title="AI Personal Tutor", layout="wide")

# Initialize the multi-page app
app = MultiPage()

# Add all your pages
app.add_page("Home", home.app)
app.add_page("Login/Register", login.app)
app.add_page("Tutor Session", tutor.app)
app.add_page("Analytics", analytics.app)
app.add_page("Profile", profile.app)

# Main app
def main():
    st.sidebar.title("Navigation")
    
    # Run the app
    app.run()

if __name__ == "__main__":
    main()