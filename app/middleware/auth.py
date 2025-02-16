import os
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv()

security = HTTPBearer()
SECRET_TOKEN = os.getenv("SECRET_TOKEN")

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    print(SECRET_TOKEN)
    if token != SECRET_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token
