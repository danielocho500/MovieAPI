from fastapi import FastAPI

from routes.user_routes import users_route
from routes.genre_routes import genre_route
from routes.artist_routes import artist_route
from routes.movies_routes import movies_route
from routes.review_routes import review_route

app = FastAPI()

app.include_router(users_route, prefix='/auth', tags=['auth'])
app.include_router(genre_route, prefix="/genre", tags=['genre'])
app.include_router(artist_route, prefix='/artist', tags=['artist'])
app.include_router(movies_route, prefix='/movie', tags=['movie'])
app.include_router(review_route, prefix='/review', tags=['review'])