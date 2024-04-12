from __future__ import annotations
from bisect import insort
from datetime import datetime
from dataclasses import dataclass
import random


@dataclass
class Activity:
    start: datetime
    end: datetime
    note: str

    def __lt__(self, other: Activity):
        return self.start < other.start

    def overlaps_with(self, other: Activity):
        return not (other.start <= self.start <= other.end or other.start <= self.end <= other.end)


@dataclass
class Page:
    date: datetime
    activities: list[Activity]

    def __lt__(self, other: Page):
        return self.date < other.date

    def delete_activity(self, index: int) -> None:
        if self.activities and 0 <= index < len(self.activities):
            del self.activities[index]

        if not self.activities:
            del self

    def add_activity(self, activity: Activity) -> None:
        insort(self.activities, activity)

    def overlapping_activities(self, activity) -> list[Activity]:
        return [_activity for _activity in self.activities if _activity.overlaps_with(activity)]

@dataclass
class Calendar:
    pages: list[Page]
    page_index: int

    def browse(self, index_delta: int) -> None:
        if not self.pages:
            return

        self.page_index = (self.page_index + index_delta) % len(self.pages)

    def delete_current_page(self) -> None:
        if not self.pages:
            return

        del self.pages[self.page_index]

        self.page_index = max(0, self.page_index - 1)

    def add_page(self, page: Page) -> None:
        insort(self.pages, page)

    def create_activity(self, date: datetime, start: datetime, end: datetime, note: str):
        new_activity = Activity(start, end, note)

        for i, page in enumerate(self.pages):
            if page.date != date:
                continue

            page.add_activity(new_activity)
            self.page_index = i
            return

        new_page = Page(date, [new_activity])
        self.add_page(new_page)
        self.page_index = self.pages.index(new_page)

    def delete_activity(self, activity: Activity):
        for i, page in enumerate(self.pages):
            if activity in page.activities:
                if len(page.activities) > 1:
                    page.activities.remove(activity)
                else:
                    self.page_index = i
                    self.delete_current_page()
                break


def generate_random_activity() -> Activity:
    day = random.randint(23, 28)
    start_hour = random.randint(0, 22)
    start_minute = random.randint(0, 58)
    end_hour = random.randint(start_hour + 1, 23)
    end_minute = random.randint(start_minute + 1, 59)

    start = datetime(2023, 10, day, start_hour, start_minute)
    end = datetime(2023, 10, day, end_hour, end_minute)
    note = random.choice(
        (
            "Meeting with team",
            "Doctor's appointment",
            "Breakfast with friends",
            "Lunch meeting",
            "Dinner date",
            "Conference call",
            "Movie night",
            "Gym workout",
            "Grocery shopping",
            "Coffee with a friend",
            "Job interview",
            "Soccer practice",
            "Family dinner",
            "Business trip",
            "Hiking adventure",
            "Shopping spree",
            "Dentist appointment",
            "Cooking class",
            "Birthday party",
            "Visit to the museum",
            "Study session",
            "Beach vacation",
            "Networking event",
            "Volunteer work",
            "Reading a good book"
        )
    )

    return Activity(start, end, note)


def get_test_calendar(activity_amount: int) -> Calendar:
    dates = {}
    for activity in [generate_random_activity() for _ in range(activity_amount)]:
        date = activity.start.date()

        if date not in dates:
            dates[date] = []

        insort(dates[date], activity)

    pages = []
    for date, activities in dates.items():
        insort(pages, Page(datetime(year=date.year, month=date.month, day=date.day), activities))

    return Calendar(pages, 0)
