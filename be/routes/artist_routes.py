from fastapi import APIRouter, Request
from models.artist import SchemaArtist
from utils.has_authorization import has_authorization, response_authorization
from utils.response_message import response_message
from db.operations.artist import exist_artist,create_artist, get_all_artist

artist_route = APIRouter()

@artist_route.post("")
def create_artist(request: Request, artist:SchemaArtist):
    
    result, _ = has_authorization(request, 1)

    if result == response_authorization.invalid_token:
        return response_message(400, "Invalid Token")
    elif result == response_authorization.no_authorization:
        return response_message(400, "No authorization")

    if (exist_artist(artist.name, artist.last_names, artist.nationality)):
        return response_message(400, "artist already exist")

    result = create_artist(artist)

    if result:
        return response_message(201, "Artist created")
    else:
        return response_message(500, "server error")
    
@artist_route.get("")
def get_artists(request: Request):

    result, _ = has_authorization(request)

    if result == response_authorization.invalid_token:
        return response_message(400, "Invalid Token")
    elif result == response_authorization.no_authorization:
        return response_message(400, "No authorization")
    
    artist = get_all_artist()

    return response_message(200, "List of all artists", {
        "artist": artist
    })