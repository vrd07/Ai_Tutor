import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Auth0Authenticator:
    def __init__(self):
        self.domain = os.getenv('AUTH0_DOMAIN')
        self.client_id = os.getenv('AUTH0_CLIENT_ID')
        self.client_secret = os.getenv('AUTH0_CLIENT_SECRET')
        self.callback_url = os.getenv('AUTH0_CALLBACK_URL', 'http://localhost:8501/callback')
        
    def get_authorize_url(self):
        """
        Generate Auth0 authorization URL
        """
        auth0_authorize_url = f'https://{self.domain}/authorize'
        oauth_client = OAuth2Session(
            self.client_id,
            self.client_secret,
            scope='openid profile email',
            redirect_uri=self.callback_url
        )
        authorization_url, _ = oauth_client.create_authorization_url(auth0_authorize_url)
        return authorization_url
    
    def get_token(self, authorization_response):
        """
        Exchange authorization code for token
        """
        token_url = f'https://{self.domain}/oauth/token'
        oauth_client = OAuth2Session(
            self.client_id,
            self.client_secret,
            scope='openid profile email',
            redirect_uri=self.callback_url
        )
        token = oauth_client.fetch_token(token_url, authorization_response=authorization_response)
        return token
    
    def get_user_info(self, token):
        """
        Retrieve user information from Auth0
        """
        user_info_url = f'https://{self.domain}/userinfo'
        headers = {'Authorization': f'Bearer {token["access_token"]}'}
        response = requests.get(user_info_url, headers=headers)
        return response.json()

def auth0_login():
    """
    Streamlit Auth0 Login Flow
    """
    authenticator = Auth0Authenticator()
    
    # Login button
    if st.button('Login with Auth0'):
        # Redirect to Auth0 login page
        authorization_url = authenticator.get_authorize_url()
        st.write('Please click the link to login:', authorization_url)
        
        # Callback handling
        authorization_response = st.text_input('Enter the full callback URL')
        if authorization_response:
            try:
                # Get token
                token = authenticator.get_token(authorization_response)
                
                # Get user info
                user_info = authenticator.get_user_info(token)
                
                # Store user info in session state
                st.session_state.user = user_info
                st.success('Login Successful!')
            except Exception as e:
                st.error(f'Login failed: {str(e)}')

def main():
    st.title('Auth0 Login')
    
    # Check if user is logged in
    if 'user' not in st.session_state:
        auth0_login()
    else:
        st.write('Welcome', st.session_state.user['name'])
        if st.button('Logout'):
            del st.session_state.user
            st.experimental_rerun()

if __name__ == '__main__':
    main()