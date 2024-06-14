import logging
from db.db import get_database
from models.movie import SchemaMovie
from bson.objectid import ObjectId
from db.operations.genre import exist_genre_by_id, get_genre_by_id
from db.operations.artist import exist_artist_by_id
from db.operations.artist import get_artist_by_id
import math

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
                movie_info["artists"].append({
                    "id": artist.id_artist,
                    "role": artist.role
                })

        db.movies.insert_one(movie_info)

        return True
    except Exception as e:
        logging.error(f'create movie: {e}')
        print(e)
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
    
def get_movies_pagination(query_movies: object, page_number: int, items_per_page: int):
    db = get_database()
    try:
        pages_total = 1

        number_movies = db.movies.count_documents(query_movies)
        if items_per_page > number_movies:
            pages_total = 1
        else:
            pages_total = math.ceil(number_movies / items_per_page)
        
        movies = db.movies.find(query_movies).skip((page_number - 1) * items_per_page).limit(items_per_page)
        return [movies, pages_total]
    except Exception as e:
        logging.error(f'get movies pagination: {e}')
        return None
    
def update_movie_cigars(id_movie: str, cigars: int) -> bool:
    db = get_database()
    try:
        movie = get_movie_details(id_movie)
        
        reviews = movie["reviews"]
        cigars_total = movie["cigars"]

        new_reviews += 1
        new_cigars = ((cigars_total * reviews) + cigars) / (reviews + 1)

        db.movies.find_one_and_update({"_id": ObjectId(id_movie)}, {"$set": {"cigars": new_cigars, "reviews": new_reviews}})

        return True
    except Exception as e:
        logging.error(f'update movie cigars: {e}')
        return False