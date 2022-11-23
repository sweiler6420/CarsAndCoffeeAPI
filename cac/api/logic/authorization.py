from enum import Enum
import orjson
from typing import Tuple, Sequence
from urllib.request import urlopen

from jose import jwt

from cac.api.exceptions import TokenError
from cac.api.config import get_settings

config_settings = get_settings()

class CRUDOperation(str, Enum):
    CREATE = 'create'
    READ = 'read'
    UPDATE = 'update'
    DELETE = 'delete'

class ResourceType(str, Enum):
    USERS = 'users'

class AuthorizationLogic:
    def get_value_from_token(self, token: str, key: str, namespace = None):
        claims = jwt.get_unverified_claims(token=token)
        if namespace:
            return claims.get(f'{namespace}{key}')
        return claims.get(f'{key}')
    
    @simple_time_cache(60*60)