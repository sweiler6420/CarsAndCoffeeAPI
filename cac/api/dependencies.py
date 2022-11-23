from typing import Tuple

from asyncpg import Pool
from databases import Database
from fastapi import Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, SecurityScopes

from cac.api.logic.authorization import AuthorizationLogic

from cac.api.exceptions import AuthError

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:zyxyTnYaOyzh8a8uDHCo@containers-us-west-54.railway.app:6853/railway"

http_bearer = HTTPBearer()
authorization_logic = AuthorizationLogic()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
