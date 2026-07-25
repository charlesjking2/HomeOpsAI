class MealBalanceEngine:
    """
    Applies weekly balance rules
    to meal selections.
    """

    def __init__(self):
        pass

    def compatible(
        self,
        previous_meal,
        next_meal,
    ):

        if previous_meal is None:
            return True

        if previous_meal.category == next_meal.category:
            return False

        return True