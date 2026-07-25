from homeops.services.household_context import HouseholdContext
from homeops.services.preference_service import PreferenceService


def test_available_equipment_loads():

    context = HouseholdContext.load()

    service = PreferenceService(
        context.household
    )

    equipment = service.available_equipment()

    assert "Smoker" in equipment
    assert "Grill" in equipment