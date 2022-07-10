from dataclasses import dataclass
from person import Person
from typing import List
from course import Course


@dataclass()
class Professor(Person):
    salary: float
    courses: List[Course]
    got_raise: bool = False

    @property
    def check_for_bonus(self):
        if len(self.courses) > 3 and not self.got_raise:
            self.got_raise = True
            return True
        return False

    def add_course(self, course):
        if not isinstance(course, Course):
            raise TypeError
        self.courses.append(course)

    def remove_course(self, course):
        if not isinstance(course, Course):
            raise TypeError
        self.courses.remove(course)
