from homeops.services.household_context import HouseholdContext
from homeops.services.preference_service import PreferenceService
from homeops.services.meal_planner import MealPlannerService


def test_meal_planner_accepts_preferences():

    context = HouseholdContext.load()

    preferences = PreferenceService(
        context.household
    )

    planner = MealPlannerService(
        context.meals,
        preferences=preferences,
    )

    assert planner.preferences.restaurant_goal() == 2