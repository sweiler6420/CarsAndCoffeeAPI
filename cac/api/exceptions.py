from typing import Optional, Dict, Any, Sequence

class UserException(Exception):
    def __init__(self, message: Optional[str] = None, tags: Optional[Dict[str, Any]] = None, extras: Optional[Dict[str, Any]] = None) -> None:
        self.message = message
        self.tags = tags or {
            'source': 'cacapi',
            'type': type(self).__name__ 
        }
        self.extra = extras or {}
        super().__init__(message)

class AuthError(UserException):
    def __init__(self, username: str, scopes: Sequence[str]) -> None:
        message = f'Unauthorized Operation For User: {username}, Security Scopes: {scopes}'
        extras = {
            'username': username,
            'scopes': scopes
        }
        super().__init__(message=message, extras=extras)