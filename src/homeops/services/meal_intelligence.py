from datetime import date, timedelta


class MealIntelligence:

    def __init__(
        self,
        rules: dict,
    ):
        self.rules = rules


    def recently_used(
        self,
        meal_name,
        history,
    ):

        days = self.rules["rotation"]["avoid_repeat_days"]

        cutoff = date.today() - timedelta(days=days)

        for meal in history:
            if (
                meal["name"] == meal_name
                and meal["date"] >= cutoff
            ):
                return True

        return False


    def score_meal(
        self,
        meal,
        history,
        favorite=False,
    ):

        score = 0

        if favorite:
            score += self.rules["scoring"]["family_favorite_bonus"]

        if self.recently_used(
            meal.name,
            history,
        ):
            score -= self.rules["scoring"]["recent_meal_penalty"]

        return score