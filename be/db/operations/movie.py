import logging
from db.db import get_database
from models.movie import SchemaMovie
from bson.objectid import ObjectId
from db.operations.genre import exist_genre_by_id, get_genre_by_id
from db.operations.artist import exist_artist_by_id
from db.operations.artist import get_artist_by_id

def exist_movie(name: str, year: int) -> bool:
    db = get_database()
    try:
        movie = db.movies.find_one({"name": name, "year": year})
        return (movie)
    except Exception as e:
        logging.error(f'movie_exist: {e}')
        return None
    
def exist_movie_by_id(id: str) -> object:
    db = get_database()
    try:
        movie = db.movies.find_one({"_id": ObjectId(id)})
        return (movie)
    except Exception as e:
        logging.error(f'movie_by_id: {e}')
        return None

def create_movie(movie: SchemaMovie):
    db = get_database()
    try:
        movie_info = {
            "name": movie.name,
            "year": movie.year,
            "cigars": 0,
            "reviews": 0,
            "genres": [],
            "artists": []
        }
        if movie.precuel_id:
            precuel = exist_movie_by_id(movie.precuel_id)
            if precuel:
                movie_info["precuel"] = str(precuel["_id"])

        for genre in movie.genres:
            if exist_genre_by_id(genre):
                movie_info["genres"].append(genre)
        
        for artist in movie.artists:
            if exist_artist_by_id(artist.id_artist):
                movie_info["artist"].append({
                    "id": artist.id_artist,
                    "role": artist.role
                })

        db.movies.insert_one(movie_info)

        return True
    except Exception as e:
        logging.error(f'create movie: {e}')
        return False
    

def get_movie_details(id_movie: str) -> object:
    try:
        movie = exist_movie_by_id(id_movie)
        print(movie)
        genres_to_return = []
        for genre_id in movie["genres"]:
            genre = get_genre_by_id(genre_id)
            if genre:
                genre["_id"] = str(genre["_id"])
                genres_to_return.append(genre)

        actresses = []
        directors = []
        for artist_object in movie["artists"]:
            artist = get_artist_by_id(artist_object["id"])
            if artist:
                artist["_id"] = str(artist["_id"])
                if artist_object["role"] == 1:
                    directors.append(artist)
                else:
                    actresses.append(artist)
        
        return {
            "name": movie["name"],
            "year": movie["year"],
            "cigars": movie["cigars"],
            "reviews": movie["reviews"],
            "genres": genres_to_return,
            "directors": directors,
            "actresses": actresses
        }
    except Exception as e:
        logging.error(f'get movie details: {e}')
        return False