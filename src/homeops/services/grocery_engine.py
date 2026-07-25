class GroceryEngine:
    """
    Converts meals into a shopping list.
    """

    def build_list(
        self,
        meals,
    ):

        ingredients = []

        for meal in meals:
            ingredients.extend(
                meal.ingredients
            )

        return sorted(
            set(ingredients)
        )