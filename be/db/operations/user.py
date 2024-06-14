import logging
from db.db import get_database
from bson.objectid import ObjectId


def register(username: str, ps:str, role: int):
    db = get_database()

    try:
        new_user = db.users.insert_one({
            "username": username,
            "ps": ps,
            "role": role
        })
        return new_user.inserted_id
    except Exception as e:
        logging.error(f'register: {e}')
        return False
    

def username_exist(username: str) -> bool:
    db = get_database()
    try:
        user = db.users.find_one({"username": username})
        return (user)
    except Exception as e:
        logging.error(f'username_exist: {e}')
        return None

def get_user_by_username(username:str):
    db = get_database()
    try:
        user = db.users.find_one({"username": username})
        return user if (user) else False
    except Exception as e:
        logging.error(f'get_user_by_username: {e}')
        return False
    
def get_user_by_id(id:str):
    db = get_database()
    try:
        user = db.users.find_one({"_id": ObjectId(id)})
        return user if (user) else False
    except Exception as e:
        logging.error(f'get_user_by_id: {e}')
        return False