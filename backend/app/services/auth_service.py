from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.user import User

# Auth0 configuration
AUTH0_DOMAIN = "your-auth0-domain"
API_AUDIENCE = "your-api-audience"
ALGORITHMS = ["RS256"]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Verify token with Auth0
        jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
        # Implement JWT validation logic here
        
        # Extract user info from token
        payload = jwt.decode(token, "", algorithms=ALGORITHMS, audience=API_AUDIENCE)
        username: str = payload.get("sub")
        
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    # Get or create user in our database
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        user = User(username=username)
        db.add(user)
        db.commit()
        db.refresh(user)
        
    return user