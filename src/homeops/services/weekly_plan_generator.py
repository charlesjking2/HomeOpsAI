from homeops.models.weekly_plan import (
    WeeklyPlan,
    PlannedMeal,
)


class WeeklyPlanGenerator:

    def __init__(
        self,
        meal_planner,
        calendar_service,
    ):
        self.meal_planner = meal_planner
        self.calendar_service = calendar_service


    def generate(
        self,
        week_start,
        schedules,
    ):

        plan = []

        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        for day, schedule in zip(days, schedules):

            busy = self.calendar_service.is_busy_day(
                schedule
            )

            meals = self.meal_planner.recommend(
                count=1,
                busy_day=busy,
            )

            meal = meals[0]

            reason = (
                "Busy night - selected easy meal"
                if busy
                else
                "Normal schedule - flexible meal"
            )

            plan.append(
                PlannedMeal(
                    day=day,
                    meal=meal.name,
                    reason=reason,
                )
            )

        return WeeklyPlan(
            week_start=week_start,
            meals=plan,
        )