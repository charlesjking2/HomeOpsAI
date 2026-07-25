from datetime import date
from pydantic import BaseModel


class MealHistoryEntry(BaseModel):
    date: date
    meal: str


class MealHistory(BaseModel):
    entries: list[MealHistoryEntry] = []