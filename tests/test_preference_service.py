from homeops.services.household_context import HouseholdContext
from homeops.services.preference_service import PreferenceService


def test_household_preferences_load():

    context = HouseholdContext.load()

    service = PreferenceService(
        context.household
    )

    assert service.restaurant_goal() == 2
    assert service.shopping_day() == "Saturday"
    assert service.meal_planning_day() == "Thursday"