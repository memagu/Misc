from dataclasses import dataclass
from enroll import Enroll
from person import Person
from typing import List


@dataclass
class Student(Person):
    international: bool
    enrolled: List[Enroll]

    @property
    def is_part_time(self):
        return len(self.enrolled) < 2

    @property
    def is_on_probation(self):
        raise NotImplementedError

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise TypeError
        self.enrolled.append(enroll)

    def remove_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise TypeError
        self.enrolled.remove(enroll)
