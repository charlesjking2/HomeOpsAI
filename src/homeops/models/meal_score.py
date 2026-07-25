from pydantic import BaseModel


class MealScore(BaseModel):
    meal_name: str
    score: int
    reasons: list[str] = []