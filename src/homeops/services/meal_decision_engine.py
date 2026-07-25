from homeops.services.meal_planner import MealPlannerService


class MealDecisionEngine:
    """
    Decides where meals should be placed
    in a weekly schedule.
    """

    def __init__(
        self,
        meal_planner: MealPlannerService,
        calendar_service=None,
    ):
        self.meal_planner = meal_planner
        self.calendar_service = calendar_service


    def build_week(
        self,
        days,
    ):

        plan = []

        for day in days:

            busy = False

            if self.calendar_service:
                busy = self.calendar_service.is_busy_day(
                    day.schedule
                )

            meals = self.meal_planner.recommend(
                count=1,
                busy_day=busy,
            )

            plan.append(
                {
                    "date": day.date,
                    "meal": meals[0],
                    "busy": busy,
                }
            )

        return plan