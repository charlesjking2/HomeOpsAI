from datetime import date

from homeops.models.meal import Meal
from homeops.models.calendar import DaySchedule

from homeops.services.meal_planner import MealPlannerService
from homeops.services.calendar_service import CalendarService
from homeops.services.weekly_plan_generator import WeeklyPlanGenerator


def test_generate_weekly_plan():

    meals = [
        Meal(
            name="Tacos",
            category="Mexican",
            prep_time_minutes=20,
            difficulty=1,
        )
    ]

    planner = MealPlannerService(
        meals
    )

    generator = WeeklyPlanGenerator(
        planner,
        CalendarService(),
    )

    schedules = [
        DaySchedule(
            date=date(2026,7,27)
        )
        for _ in range(7)
    ]

    result = generator.generate(
        date(2026,7,27),
        schedules,
    )

    assert result.meal_count == 7
    assert result.meals[0].meal == "Tacos"