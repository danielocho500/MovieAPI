from pydantic import BaseModel, Field

class SchemaUser(BaseModel):
    username: str = Field(min_length=8, max_length=20)
    ps: str = Field(min_length=8, max_length=30)
    role: int = Field(ge=1, le=3)
