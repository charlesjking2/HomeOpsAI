from homeops.models.meal import Meal
from homeops.services.meal_planner import MealPlannerService
from homeops.services.memory_service import MemoryService


def test_recent_meals_score_lower():

    meals = [
        Meal(
            name="Tacos",
            category="Mexican",
            family_rating=5,
        ),
        Meal(
            name="Chicken Fajita",
            category="Mexican",
            family_rating=4,
        ),
    ]

    memory = MemoryService(":memory:")

    memory.add_meal(
        "Tacos",
        "2026-07-24",
    )

    planner = MealPlannerService(
        meals,
        memory,
    )

    result = planner.recommend(
        count=1
    )

    assert result[0].name == "Chicken Fajita"