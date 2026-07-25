from homeops.models.meal import Meal


class MealPlannerService:
    """
    Scores meals based on household needs.
    """

    def __init__(
        self,
        meals: list[Meal],
    ):
        self.meals = meals

    def score_meal(
        self,
        meal: Meal,
        busy_day: bool = False,
    ) -> int:

        score = 0

        # Family preference
        score += meal.family_rating

        # Busy nights favor quick meals
        if busy_day:
            if meal.prep_time_minutes <= 30:
                score += 5
            else:
                score -= 3

        # Easy meals get priority
        if meal.difficulty <= 2:
            score += 2

        # Lunch awareness
        if meal.makes_leftovers:
            score += 1

        return score


    def recommend(
        self,
        count: int = 5,
        busy_day: bool = False,
    ) -> list[Meal]:

        ranked = sorted(
            self.meals,
            key=lambda meal:
                self.score_meal(
                    meal,
                    busy_day
                ),
            reverse=True,
        )

        return ranked[:count]