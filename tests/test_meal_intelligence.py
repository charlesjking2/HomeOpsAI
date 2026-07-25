from datetime import date

from homeops.services.meal_intelligence import (
    MealIntelligence,
)


def test_recent_meal_penalty():

    rules = {
        "rotation": {
            "avoid_repeat_days": 14
        },
        "scoring": {
            "family_favorite_bonus": 5,
            "recent_meal_penalty": 10,
        },
    }


    intelligence = MealIntelligence(
        rules
    )


    history = [
        {
            "name": "Tacos",
            "date": date.today(),
        }
    ]


    assert intelligence.recently_used(
        "Tacos",
        history,
    )