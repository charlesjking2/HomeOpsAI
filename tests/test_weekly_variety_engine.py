from homeops.services.weekly_variety_engine import WeeklyVarietyEngine


class FakeMemory:

    def recently_used(
        self,
        meal_name
    ):
        return meal_name == "Tacos"



def test_recent_meals_are_filtered():

    engine = WeeklyVarietyEngine(
        FakeMemory()
    )

    meals = [
        type(
            "Meal",
            (),
            {"name": "Tacos"}
        )(),
        type(
            "Meal",
            (),
            {"name": "Chicken Shawarma"}
        )(),
    ]

    result = engine.filter_recent(
        meals
    )

    assert len(result) == 1
    assert result[0].name == "Chicken Shawarma"