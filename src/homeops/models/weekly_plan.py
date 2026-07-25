from datetime import date
from pydantic import BaseModel


class PlannedMeal(BaseModel):
    day: str
    meal: str
    reason: str = ""


class WeeklyPlan(BaseModel):
    week_start: date
    meals: list[PlannedMeal]

    @property
    def meal_count(self):
        return len(self.meals)