from fastapi import APIRouter, Request
from utils.has_authorization import has_authorization, response_authorization
from models.movie import SchemaMovie
from utils.response_message import response_message
from db.operations.movie import exist_movie, create_movie, exist_movie_by_id, get_movie_details, get_movies_pagination

movies_route = APIRouter()

@movies_route.post("")
def create(request: Request, movie: SchemaMovie):
    result, _ = has_authorization(request, 1)

    if result == response_authorization.invalid_token:
        return response_message(400, "Invalid Token")
    elif result == response_authorization.no_authorization:
        return response_message(400, "No authorization")
    
    if exist_movie(movie.name, movie.year):
        return response_message(400, "movie already exist")
    
    if create_movie(movie):
        return response_message(201, "Movie Crated")
    else:
        return response_message(500, "Server Error")
    
@movies_route.get("/{movie_id}")
def get_movie(request: Request, movie_id: str):
    result, _ = has_authorization(request)

    if result == response_authorization.invalid_token:
        return response_message(400, "Invalid Token")
    elif result == response_authorization.no_authorization:
        return response_message(400, "No authorization")
    
    if not exist_movie_by_id(movie_id):
        return response_message(404, "movie not found")

    movie = get_movie_details(movie_id)
    return response_message(200, "movie found", {
        "movie": movie
    })


@movies_route.get("/")
def get_movies(request: Request, artist_id: str = None, movie_name: str = None, year: int = None, rating_more: float = None, rating_less: float = None, page_number: int = 1, items_per_page: int = 3 ):
    query_movies = {}

    if artist_id:
        query_movies["artists"] = {
            "$elemMatch": {
                "id": artist_id,
                "role": {"$in": [1, 2]}
            }
        }
        
    if movie_name:
        query_movies["name"] = {"$regex": movie_name, "$options": "i"}

    if year:
        query_movies["year"] = 2019

    movies, pages_total = get_movies_pagination(query_movies, page_number, items_per_page)

    movies_to_return = []

    for movie in movies:
        movie_details = get_movie_details(str(movie["_id"]))
        movies_to_return.append(movie_details)

    return response_message(200, "movies found", {
        "pages_total": pages_total,
        "movies": movies_to_return
    })


