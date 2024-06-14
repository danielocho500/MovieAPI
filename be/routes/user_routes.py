import logging
from fastapi import APIRouter
from models.user import SchemaUser
from models.login import SchemaLogin
from db.operations.user import register, username_exist, get_user_by_username
from utils.response_message import response_message
from utils.password import is_secure_psd, hash_password, check_password
from utils.jwt import encode_jwt

users_route = APIRouter()

@users_route.post("/register")
def register_user(user: SchemaUser):
    username_exist_result = username_exist(user.username)
    if username_exist_result or username_exist_result != None:
        return response_message(code=409,message="The user is already registered", data={})
    
    if not is_secure_psd(user.ps):
        return response_message(400, "The password should contain an upper letter, a symbol and a number", {})

    hashed = hash_password(user.ps)

    new_user_id = register(user.username, hashed, user.role)

    jwt = encode_jwt(new_user_id)

    if new_user_id:
        return response_message(201, "created", {
            "acces-token":  jwt
        })
    else:
        return response_message(500, "Server error")
    

@users_route.post("/login")
def login(login: SchemaLogin):
    user = get_user_by_username(login.username)
    if not user:
        return response_message(400, "Incorrect username or password")
    
    if not check_password(login.ps, user["ps"]):
        return response_message(400, "Incorrect username or password")
    
    jwt = encode_jwt(str(user["_id"]))

    return response_message(201, "logged", {
        "acces-token":  jwt
    })


    
