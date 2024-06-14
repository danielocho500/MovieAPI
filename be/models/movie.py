from datetime import datetime
from pydantic import BaseModel, Field

class SchemaArtistMovie(BaseModel):
    id_artist: str
    role: int = Field(ge=1, le=2)

class SchemaMovie(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    genres: list[str]
    artists: list[SchemaArtistMovie]
    precuel_id: str = Field(None)
    year: int = Field(ge=1800, le=2100)

