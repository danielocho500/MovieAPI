from pydantic import BaseModel, Field

class SchemaLogin(BaseModel):
    username: str = Field(min_length=8,max_length=60)
    ps: str = Field(min_length=8, max_length=20)