from dataclasses import dataclass
from datetime import date
from enroll import Enroll
from professor import Professor
from typing import List


@dataclass
class Course:
    name: str
    code: str
    max_students: int
    min_students: int
    start: date
    end: date
    professors: List[Professor]
    enrollments: List[Enroll]

    @property
    def is_cancelled(self):
        return len(self.enrollments) < self.min_students

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise TypeError
        self.professors.append(professor)

    def remove_professor(self, professor):
        if not isinstance(professor, Professor):
            raise TypeError
        self.professors.remove(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise TypeError
        self.enrollments.append(enroll)

    def remove_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise TypeError
        self.enrollments.remove(enroll)
