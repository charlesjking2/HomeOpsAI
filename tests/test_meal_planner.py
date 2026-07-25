from homeops.models.meal import Meal
from homeops.services.meal_planner import MealPlannerService


def test_busy_day_prefers_quick_meals():

    meals = [
        Meal(
            name="Brisket",
            category="BBQ",
            prep_time_minutes=480,
            difficulty=4,
        ),
        Meal(
            name="Tacos",
            category="Mexican",
            prep_time_minutes=20,
            difficulty=1,
        ),
    ]

    planner = MealPlannerService(meals)

    recommendations = planner.recommend(
        count=1,
        busy_day=True,
    )

    assert recommendations[0].name == "Tacos"