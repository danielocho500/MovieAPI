import logging
from models.genre import SchemaGenre
from db.db import get_database
from bson.objectid import ObjectId

def exist_genre_by_name(name: str) -> bool:
    db = get_database()
    try:
        genre = db.genres.find_one({"name": name})
        return (genre)
    except Exception as e:
        logging.error(f'genre_exist: {e}')
        return None
    
def get_genre_by_id(id:str) -> object:
    db = get_database()
    try:
        genre = db.genres.find_one({"_id": ObjectId(id)})
        return genre
    except Exception as e:
        logging.error(f'genre_exist: {e}')
        return None
    
def exist_genre_by_id(id: str) -> bool:
    db = get_database()
    try:
        genre = db.genres.find_one({"_id": ObjectId(id)})
        return (genre)
    except Exception as e:
        logging.error(f'genre_exist: {e}')
        return None    
    
def all_exist_genre(ids: list[str]) -> str:
    db = get_database()
    flag = True
    id_not_found = ""
    try:
        for id_genre in ids:
            exist = db.genres.find_one({"_id": ObjectId(id)})   
            if not exist:
                flag = False
                id_not_found = id_genre
                break

        return str(1) if flag else id_not_found
    except Exception as e:
        logging.error(f'genre_all_exist: {e}')
        return None



def create_genre(genre: SchemaGenre) -> bool:
    db = get_database()
    try:
        db.genres.insert_one({
            "name": genre.name,
            "description": genre.description
        })
        return True
    except Exception as e:
        logging.error(f'create genre: {e}')
        return False
    

def get_all_genre() -> list[object]:
    db = get_database()
    genres_to_return = []
    try:
        genres = db.genres.find()
        for genre in genres:
            genres_to_return.append({
                "id": str(genre["_id"]),
                "name": genre["name"],
                "description": genre["description"]
            })
        
        return genres_to_return
    except Exception as e:
        logging.error(f'get_genres: {e}')
        return None