from pydantic import BaseModel, Field
from typing import Optional, Annotated

class User(BaseModel):
    id: str = Field( description="User ID")
    username: str
    email: str
    password: str