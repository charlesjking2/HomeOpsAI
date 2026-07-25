from homeops.models.meal import Meal


class MealPlannerService:

    def __init__(
        self,
        meals: list[Meal],
        memory=None,
    ):
        self.meals = meals
        self.memory = memory


    def score_meal(
        self,
        meal: Meal,
        busy_day: bool = False,
    ) -> int:

        score = 0

        score += meal.family_rating

        if busy_day:
            if meal.prep_time_minutes <= 30:
                score += 5
            else:
                score -= 3

        if meal.difficulty <= 2:
            score += 2

        if meal.makes_leftovers:
            score += 1

        # New memory awareness
        if self.memory:
            if self.memory.recently_used(
                meal.name
            ):
                score -= 5

        return score


    def recommend(
        self,
        count=5,
        busy_day=False,
    ):

        ranked = sorted(
            self.meals,
            key=lambda meal:
                self.score_meal(
                    meal,
                    busy_day,
                ),
            reverse=True,
        )

        return ranked[:count]