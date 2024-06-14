from datetime import datetime
from pydantic import BaseModel, Field

class SchemaGenre(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    description: str = Field("A very exiting genre", min_length=10, max_length=200)