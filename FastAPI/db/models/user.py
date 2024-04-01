
## User Model ##

from pydantic import BaseModel,Field
from typing import Optional



class User(BaseModel):
    id: Optional[str] = Field(None, description="Unique user identifier")
    username: str
    email: str
