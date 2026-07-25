from homeops.models.meal import Meal
from homeops.services.meal_intelligence import MealIntelligence


def test_favorite_quick_meal_scores_high():

    rules = {
        "rotation": {
            "avoid_repeat_days": 14
        },
        "scoring": {
            "family_favorite_bonus": 5,
            "recent_meal_penalty": 10,
        },
    }


    meal = Meal(
        name="Tacos",
        category="Mexican",
        proteins=["beef"],
        equipment=["stove"],
        tags=["quick"],
    )


    intelligence = MealIntelligence(
        rules
    )


    result = intelligence.rank_meal(
        meal,
        history=[],
        favorite=True,
        busy_day=True,
    )


    assert result.score == 8
    assert "Family favorite" in result.reasons