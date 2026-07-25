from homeops.services.meal_balance_engine import MealBalanceEngine


class Meal:
    def __init__(self, name, category):
        self.name = name
        self.category = category


def test_different_categories_are_allowed():

    engine = MealBalanceEngine()

    tacos = Meal(
        "Tacos",
        "Mexican"
    )

    brisket = Meal(
        "Brisket",
        "BBQ"
    )

    assert engine.compatible(
        tacos,
        brisket
    )