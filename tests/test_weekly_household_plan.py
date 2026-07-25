from homeops.services.weekly_household_plan import WeeklyHouseholdPlan


class MockMealEngine:
    def generate(self):
        return [
            {
                "name": "Tacos",
                "ingredients": [
                    "Chicken",
                    "Tortillas",
                ],
            },
            {
                "name": "Brisket",
                "ingredients": [
                    "Beef",
                    "Rice",
                ],
            },
        ]


class MockGroceryEngine:
    def build_list(
        self,
        meals,
    ):
        ingredients = []

        for meal in meals:
            ingredients.extend(
                meal["ingredients"]
            )

        return sorted(
            set(ingredients)
        )


class MockStorePlanner:
    def assign_store(
        self,
        item,
    ):

        if item == "Beef":
            return "Costco"

        return "Meijer"


def test_weekly_household_plan_combines_services():

    planner = WeeklyHouseholdPlan(
        meal_engine=MockMealEngine(),
        grocery_engine=MockGroceryEngine(),
        store_planner=MockStorePlanner(),
    )

    result = planner.generate()

    assert len(result["meals"]) == 2

    assert result["shopping"] == {
        "Costco": [
            "Beef",
        ],
        "Meijer": [
            "Chicken",
            "Rice",
            "Tortillas",
        ],
    }