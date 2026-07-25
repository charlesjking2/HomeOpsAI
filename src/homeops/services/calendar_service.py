from homeops.models.calendar import DaySchedule


class CalendarService:

    def is_busy_day(
        self,
        schedule: DaySchedule,
        threshold=3,
    ) -> bool:

        return schedule.busy_score >= threshold


    def dinner_complexity(
        self,
        schedule: DaySchedule,
    ) -> str:

        if schedule.busy_score >= 4:
            return "easy"

        if schedule.busy_score >= 2:
            return "moderate"

        return "complex"