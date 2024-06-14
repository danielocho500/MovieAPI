from fastapi import Request
from utils.jwt import get_id_from_jwt
from utils.response_message import response_message
from db.operations.user import get_user_by_id
from enum import Enum

class response_authorization(Enum):
    success = 0
    invalid_token = 1,
    no_authorization = 2
    server_error = -1

def has_authorization(request: Request, role: int = 0 ) -> tuple[response_authorization, int]:
    acces_token = request.headers.get("access-token")
    user_id = get_id_from_jwt(acces_token)

    if user_id == -1 or not user_id:
        return [response_authorization.invalid_token, -1]
    elif user_id == None:
        return [response_authorization.server_error, -1]
    
    user = get_user_by_id(user_id)

    if not user:
        return [response_authorization.invalid_token, -1]

    if role != 0:
        if not user["role"] == role:
            return [response_authorization.no_authorization, -1]
    
    return [response_authorization.success, user_id]