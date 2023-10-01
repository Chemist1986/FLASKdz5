from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int = Field(ge=0)
    title: str = Field(max_length=50)
    description: str = Field(max_length=100)
    status: bool = Field(default=False)