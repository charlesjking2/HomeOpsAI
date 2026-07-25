from datetime import date

from homeops.models.calendar import (
    CalendarEvent,
    DaySchedule,
)

from homeops.services.calendar_service import (
    CalendarService,
)


def test_busy_schedule_requires_easy_meal():

    schedule = DaySchedule(
        date=date(2026,7,28),
        events=[
            CalendarEvent(
                person="Trey",
                title="Robotics",
                date=date(2026,7,28),
                start_time="17:00",
                end_time="20:00",
                category="activity",
            ),
            CalendarEvent(
                person="Heidi",
                title="Soccer",
                date=date(2026,7,28),
                start_time="18:00",
                end_time="19:30",
                category="sports",
            ),
        ],
    )

    service = CalendarService()

    assert service.is_busy_day(schedule)

    assert service.dinner_complexity(schedule) == "easy"