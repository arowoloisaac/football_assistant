from pydantic import BaseModel, Field
from typing import Optional, Annotated, List

class Analysis(BaseModel):
    title: Annotated[str, Field()]
    description: str = Field()
    videoUrl: Annotated[str, Field()]