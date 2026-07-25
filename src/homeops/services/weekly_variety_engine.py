from homeops.models.meal import Meal


class WeeklyVarietyEngine:
    """
    Applies weekly planning rules
    to avoid repetitive meal plans.
    """

    def __init__(
        self,
        memory=None,
    ):
        self.memory = memory


    def filter_recent(
        self,
        meals: list[Meal],
    ) -> list[Meal]:

        if not self.memory:
            return meals

        return [
            meal
            for meal in meals
            if not self.memory.recently_used(
                meal.name
            )
        ]