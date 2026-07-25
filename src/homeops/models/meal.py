from pydantic import BaseModel
from typing import List


class Meal(BaseModel):
    name: str
    category: str

    proteins: List[str] = []
    equipment: List[str] = []

    tags: List[str] = []

    prep_time_minutes: int = 30
    difficulty: int = 2

    makes_leftovers: bool = False

    family_rating: int = 0

    notes: str = ""