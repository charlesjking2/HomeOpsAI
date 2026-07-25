from homeops.services.grocery_engine import GroceryEngine


class Meal:

    def __init__(
        self,
        name,
        ingredients,
    ):
        self.name = name
        self.ingredients = ingredients


def test_combines_meal_ingredients():

    engine = GroceryEngine()

    meals = [
        Meal(
            "Tacos",
            [
                "Tortillas",
                "Chicken",
            ],
        ),
        Meal(
            "Chicken Wraps",
            [
                "Chicken",
                "Lettuce",
            ],
        ),
    ]

    result = engine.build_list(
        meals
    )

    assert result == [
        "Chicken",
        "Lettuce",
        "Tortillas",
    ]