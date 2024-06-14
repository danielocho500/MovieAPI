from datetime import datetime
from pydantic import BaseModel, Field

class SchemaReview(BaseModel):
    user: str
    movie: str
    cigars: int
    created_at: datetime = Field(datetime.now)