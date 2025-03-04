from fastapi import Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
import os

class AuthMiddleware:
    def __init__(self):
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
        self.AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
        self.API_AUDIENCE = os.getenv('AUTH0_AUDIENCE')
        self.ALGORITHMS = ["RS256"]

    async def verify_token(self, token: str):
        """
        Verify JWT token from Auth0
        """
        try:
            # Fetch JSON Web Key Set (JWKS)
            jwks_url = f'https://{self.AUTH0_DOMAIN}/.well-known/jwks.json'
            jwks_client = jwt.PyJWKClient(jwks_url)
            
            # Decode and verify the token
            signing_key = jwks_client.get_signing_key_from_jwt(token)
            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=self.ALGORITHMS,
                audience=self.API_AUDIENCE,
                issuer=f'https://{self.AUTH0_DOMAIN}/'
            )
            return payload
        except JWTError:
            raise HTTPException(status_code=401, detail="Could not validate credentials")

    def get_current_user(self, request: Request):
        """
        Extract current user from session or token
        """
        # Check session-based authentication
        user = request.session.get('user')
        if user:
            return user

        # Check token-based authentication
        token = self.oauth2_scheme(request)
        if token:
            return self.verify_token(token)

        raise HTTPException(status_code=401, detail="Not authenticated")

# Dependency for route protection
auth_middleware = AuthMiddleware()
def protected_route(request: Request):
    return auth_middleware.get_current_user(request)