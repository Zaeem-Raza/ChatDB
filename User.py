from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., description="The unique identifier for the user")
    name: str = Field(..., description="The name of the user")
    age: int = Field(gt=0, lt=100, description="The age of the user")