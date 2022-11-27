from typing import Optional

from pydantic import BaseModel

class Word(BaseModel):
    content: str
    stressed_letter: Optional[int]
    difficulty: Optional[int]
    part_of_speech: Optional[str]
