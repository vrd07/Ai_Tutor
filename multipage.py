import streamlit as st

class MultiPage:
    def __init__(self):
        self.pages = {}
        self.current_page = None

    def add_page(self, title, func):
        """
        Add a new page to the application
        
        Args:
            title (str): Page title
            func (callable): Page function to render
        """
        self.pages[title] = func

    def run(self):
        """
        Render the selected page
        """
        # Sidebar page selection
        page = st.sidebar.radio("Navigate", list(self.pages.keys()))
        
        # Store current page in session state
        st.session_state.current_page = page
        
        # Run the selected page function
        self.pages[page]()