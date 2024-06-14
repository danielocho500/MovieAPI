from fastapi import APIRouter, Request
from utils.has_authorization import has_authorization, response_authorization
from models.movie import SchemaMovie
from utils.response_message import response_message
from db.operations.movie import exist_movie, create_movie, exist_movie_by_id, get_movie_details


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