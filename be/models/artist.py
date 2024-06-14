from datetime import datetime
from pydantic import BaseModel, Field

class SchemaArtist(BaseModel):
    name: str = Field( min_length=1, max_length=40)
    last_names: str = Field(min_length=1, max_length=80)
    nationality: str = Field(max_length=80)