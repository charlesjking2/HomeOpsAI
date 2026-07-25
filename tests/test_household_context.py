from homeops.services.household_context import HouseholdContext


def test_household_context_loads():

    context = HouseholdContext.load()

    summary = context.summary()

    assert summary["family_size"] == 6
    assert summary["restaurant_goal"] == 2
    assert summary["meal_count"] > 0