import logging
from models.artist import SchemaArtist
from db.db import get_database
from bson.objectid import ObjectId

def exist_artist(name: str, last_names: str, nationality: str) -> bool:
    db = get_database()
    try:
        artist = db.artists.find_one({"name": name, "last_names": last_names, "nationality": nationality})
        return (artist)
    except Exception as e:
        logging.error(f'artist_exist: {e}')
        return None
    
def exist_artist_by_id(id: str) -> bool:
    db = get_database()
    try:
        artist = db.artists.find_one({"_id": ObjectId(id)})
        return (artist)
    except Exception as e:
        logging.error(f'artist_exist: {e}')
        return None
    
def get_artist_by_id(id: str):
    print(f'aqui {id}')
    db = get_database()
    try:          
        artist = db.artists.find_one({"_id": ObjectId(id)})
        if artist:
            print(f'artist: {artist}')
            return artist
    except Exception as e:
        logging.error(f'get_artist: {e}')
        return None

def create_artist(artist: SchemaArtist) -> bool:
    db = get_database()
    try:
        db.artists.insert_one({
            "name": artist.name,
            "last_names": artist.last_names,
            "nationality": artist.nationality
        })
        return True
    except Exception as e:
        logging.error(f'create artist: {e}')
        return False
    

def get_all_artist() -> list[object]:
    db = get_database()
    artists_to_return = []
    try:
        artists = db.artists.find()
        for artist in artists:
            artists_to_return.append({
                "id": str(artist["_id"]),
                "name": artist["name"],
                "last_names": artist["last_names"],
                "nationality": artist["nationality"]
            })
        
        return artists_to_return
    except Exception as e:
        logging.error(f'get_artists: {e}')
        return None