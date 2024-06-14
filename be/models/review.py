from datetime import datetime
from pydantic import BaseModel, Field

class SchemaReview(BaseModel):
    movie_id: str
    description: str = Field(max_length=500)
    cigars: int = Field(gt=1, lt=6)