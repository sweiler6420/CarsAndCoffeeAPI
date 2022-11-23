from functools import lru_cache
import json
from typing import Optional, Dict, Any
from pydantic import BaseSettings
from enum import Enum
import os
import logging
import jwt

from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0

#determine environment
# env = (os.environ.get('API_ENV') or 'local').lower()

# class Environment(str, Enum):
#     PRODUCTION = 'prod'
#     DEVELOPMENT = 'dev'
#     LOCAL = 'local'
#     LOCAL_DOCKER = 'local_docker'

# def get_log_level():
#     """
#     return appropriate log level
#     """
#     if env in [Environment.LOCAL, Environment.LOCAL_DOCKER]:
#         return logging.DEBUG
#     else:
#         return logging.WARNING



def get_secret() -> Dict[str, Any]:
    filename = os.path.join('secrets.json')
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}

def configure_db_connection() -> str:
    secret = get_secret()

    db_host = secret.get('DB_HOST')
    db_port = secret.get('DB_PORT')
    db_name = secret.get('DB_NAME')
    db_user = secret.get('DB_USER')
    db_password = secret.get('DB_PASSWORD')

    return f'postgresql://${db_user}:${db_password}@${db_host}:${db_port}/${db_name}'

def get_auth() -> str:
    secret= get_secret()

    domain = secret.get('AUTH0_DOMAIN')
    client_id = secret.get('CLIENT_ID')
    client_secret = secret.get('CLIENT_SECRET')
    api_audience = secret.get('API_AUDIENCE')

    token = GetToken(domain)

    mgmt_resp = token.client_credentials(client_id=client_id, client_secret=client_secret, audience=api_audience)

    mgmt_api_token = mgmt_resp['access_token']

    return mgmt_api_token

class Settings(BaseSettings):
    # API CONFIG SETTINGS
    API_VERSION: str = '1.0.0'
    API_MAJOR_VERSION: str = API_VERSION.split('.')[0]
    API_TITLE: str = f'Cars and Coffee - v{API_MAJOR_VERSION}'

    # DB CONNECTION POOL CONFIG SETTINGS
    MIN_DB_POOL_SIZE: int = 1
    MAX_DB_POOL_SIZE: int = 1

    # ES CONFIG SETTINGS
    SEARCH_ENABLED: bool = False
    SEARCH_QUEUE_URL: str = ''
    SEARCH_INDEX_NAMES: Dict[str, str] = {}

    # CORS config settings
    ALLOW_ORIGIN_REGEX: str = 'https://.*\.townhouse_dev\.com'

    # AUTH0
    ALGORITHMS = ["RS256"]

def get_settings() -> BaseSettings:
    return Settings()