import jwt, logging, os
from datetime import datetime, timedelta, timezone

def encode_jwt(user_id: str, expiration_minutes: int = 36000) -> str:

    secret_key_jwt = os.environ.get("SECRET_JWT") 
    
    expiration_time = datetime.now(timezone.utc) + timedelta(minutes=expiration_minutes)
    
    encoded_jwt = jwt.encode({
        "id": str(user_id),
        "exp": expiration_time
    }, secret_key_jwt, algorithm="HS256")
    
    return encoded_jwt

def get_id_from_jwt(access_token:str):
    secret_key_jwt = os.environ.get("SECRET_JWT") 
    try:
        jwt_decoded = jwt.decode(access_token, secret_key_jwt, algorithms=["HS256"])

        if jwt_decoded["id"]:
            return jwt_decoded["id"]
        else:
            return -1
    except Exception as e:
        logging.error(f'username_exist: {e}')
        return None
