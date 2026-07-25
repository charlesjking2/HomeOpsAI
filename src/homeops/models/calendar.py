from datetime import date
from pydantic import BaseModel


class CalendarEvent(BaseModel):
    person: str
    title: str
    date: date
    start_time: str
    end_time: str
    category: str = "other"


class DaySchedule(BaseModel):
    date: date
    events: list[CalendarEvent] = []

    @property
    def busy_score(self):
        score = 0

        for event in self.events:
            if event.category in [
                "sports",
                "school",
                "work",
                "activity",
            ]:
                score += 2

        return score