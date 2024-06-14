from datetime import datetime
from pydantic import BaseModel, Field

class SchemaParticipate(BaseModel):
    movie: str
    artist: str