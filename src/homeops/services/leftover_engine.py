class LeftoverEngine:
    """
    Applies leftover strategy rules.
    """

    def creates_lunch_leftovers(
        self,
        meal,
    ):
        return meal.makes_leftovers


    def should_prefer(
        self,
        meal,
        busy_day=False,
    ):

        if busy_day and meal.makes_leftovers:
            return True

        return False