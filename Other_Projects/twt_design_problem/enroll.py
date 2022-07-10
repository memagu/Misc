from course import Course
from dataclasses import dataclass
from datetime import date
from student import Student


@dataclass
class Enroll:
    student: Student
    course: Course
    enroll_date: date
    course_grade: float = None

    def set_grade(self, grade):
        self.grade = grade