from fastapi import FastAPI

from routes.user_routes import users_route
from routes.genre_routes import genre_route
from routes.artist_routes import artist_route
from routes.movies_routes import movies_route

app = FastAPI()

app.include_router(users_route, prefix='/auth')
app.include_router(genre_route, prefix="/genre")
app.include_router(artist_route, prefix='/artist')
app.include_router(movies_route, prefix='/movie')