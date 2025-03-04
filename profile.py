import streamlit as st

def app():
    """
    User Profile Page
    """
    st.title("User Profile")
    
    # Check authentication
    if 'authenticated' not in st.session_state or not st.session_state.get('authenticated'):
        st.warning("Please log in to view your profile.")
        return
    
    # Profile information
    st.header(f"Welcome, {st.session_state.get('username', 'User')}")
    
    # Profile sections
    tab1, tab2, tab3 = st.tabs(["Personal Info", "Learning Goals", "Settings"])
    
    with tab1:
        st.subheader("Personal Information")
        
        # Profile picture upload
        profile_pic = st.file_uploader("Upload Profile Picture", type=['png', 'jpg', 'jpeg'])
        
        # User details
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name", value=st.session_state.get('username', ''))
            email = st.text_input("Email Address")
        
        with col2:
            last_name = st.text_input("Last Name")
            phone = st.text_input("Phone Number")
        
        # Save profile button
        if st.button("Save Profile"):
            st.success("Profile updated successfully!")
    
    with tab2:
        st.subheader("Learning Goals")
        
        # Learning preferences
        subjects = st.multiselect(
            "Subjects of Interest", 
            ["Mathematics", "Science", "Programming", "Languages", "History", "Arts"],
            default=["Programming", "Mathematics"]
        )
        
        learning_level = st.selectbox(
            "Current Learning Level", 
            ["Beginner", "Intermediate", "Advanced"],
            index=1
        )
        
        # Learning goals
        learning_goals = st.text_area(
            "Set Your Learning Goals", 
            "I want to improve my programming skills and learn advanced algorithm design."
        )
        
        # Save goals button
        if st.button("Save Learning Goals"):
            st.success("Learning goals updated!")
    
    with tab3:
        st.subheader("Account Settings")
        
        # Notification preferences
        st.write("Notification Preferences")
        email_notifications = st.checkbox("Receive Email Notifications", value=True)
        sms_notifications = st.checkbox("Receive SMS Notifications")
        
        # Theme selection
        theme = st.selectbox(
            "App Theme", 
            ["Light", "Dark"],
            index=0
        )
        
        # Privacy settings
        st.write("Privacy Settings")
        profile_visibility = st.radio(
            "Profile Visibility", 
            ["Public", "Private"],
            index=1
        )
        
        # Change password
        st.subheader("Change Password")
        current_password = st.text_input("Current Password", type="password")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm New Password", type="password")
        
        # Save settings button
        if st.button("Save Settings"):
            # Password change validation
            if new_password and new_password != confirm_password:
                st.error("New passwords do not match!")
            else:
                st.success("Account settings updated successfully!")