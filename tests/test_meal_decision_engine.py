from datetime import date

from homeops.models.meal import Meal
from homeops.services.meal_planner import MealPlannerService
from homeops.services.meal_decision_engine import MealDecisionEngine


class FakeDay:

    def __init__(self, day):
        self.date = day
        self.schedule = None



def test_engine_builds_week():

    meals = [
        Meal(
            name="Tacos",
            category="Mexican",
            prep_time_minutes=20,
            difficulty=1,
        )
    ]

    planner = MealPlannerService(meals)

    engine = MealDecisionEngine(
        planner
    )

    days = [
        FakeDay(
            date(2026,7,27)
        )
    ]

    result = engine.build_week(days)

    assert len(result) == 1
    assert result[0]["meal"].name == "Tacos"