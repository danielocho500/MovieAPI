from fastapi import APIRouter, Request
from models.genre import SchemaGenre
from utils.response_message import response_message
from utils.has_authorization import has_authorization, response_authorization
from db.operations.genre import create_genre, exist_genre_by_id, get_all_genre

genre_route = APIRouter()

@genre_route.post("")
def create_genre(request: Request, genre: SchemaGenre):
    
    result, _ = has_authorization(request, 1)

    if result == response_authorization.invalid_token:
        return response_message(400, "Invalid Token")
    elif result == response_authorization.no_authorization:
        return response_message(400, "No authorization")

    if (exist_genre_by_id(genre.name)):
        return response_message(400, "genre already exist")

    result = create_genre(genre)

    if result:
        return response_message(201, "Genre created")
    else:
        return response_message(500, "server error")
    
@genre_route.get("")
def get_genres(request: Request):

    result, _ = has_authorization(request)

    if result == response_authorization.invalid_token:
        return response_message(400, "Invalid Token")
    elif result == response_authorization.no_authorization:
        return response_message(400, "No authorization")
    
    genres = get_all_genre()

    return response_message(200, "List of all genres", {
        "genres": genres
    })