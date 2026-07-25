from pydantic import BaseModel
from typing import List


class Meal(BaseModel):
    name: str
    category: str
    proteins: List[str] = []
    equipment: List[str] = []
    family_rating: int = 0
    prep_time_minutes: int = 30
    difficulty: int = 1
    makes_leftovers: bool = False
    notes: str = ""