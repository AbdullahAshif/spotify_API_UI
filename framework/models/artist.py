from typing import List
from pydantic import BaseModel


class Artist(BaseModel):
    id: str
    name: str
    genres: List[str]
    songs: List[str]
