from homeops.models.meal import Meal
from homeops.services.meal_planner import MealPlannerService
from homeops.services.preference_service import PreferenceService
from homeops.services.household_context import HouseholdContext


def test_leftover_policy_affects_scoring():

    context = HouseholdContext.load()

    preferences = PreferenceService(
        context.household
    )

    meal = Meal(
        name="Brisket",
        category="BBQ",
        prep_time_minutes=480,
        difficulty=4,
        makes_leftovers=True,
    )

    planner = MealPlannerService(
        [meal],
        preferences=preferences,
    )

    score = planner.score_meal(meal)

    assert score < meal.family_rating + 2