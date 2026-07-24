from pydantic import BaseModel
from typing import List


class Appliance(BaseModel):
    name: str
    available: bool = True
    notes: str = ""


class Store(BaseModel):
    name: str
    priority: int
    notes: str = ""


class HouseholdPreferences(BaseModel):
    restaurant_goal_per_week: int
    leftovers_policy: str
    meal_planning_day: str
    shopping_day: str


class Household(BaseModel):
    family_name: str
    family_size: int
    stores: List[Store]
    appliances: List[Appliance]
    preferences: HouseholdPreferences
