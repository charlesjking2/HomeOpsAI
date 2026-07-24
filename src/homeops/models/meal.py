from pydantic import BaseModel
from typing import List


class Meal(BaseModel):
    name: str
    category: str
    proteins: List[str]
    equipment: List[str]
    family_rating: int = 0
    notes: str = ""
