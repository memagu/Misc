from adress import Address
from course import Course
from enroll import Enroll
from person import Person
from professor import Professor
from student import Student
from datetime import date

p = Person("a", "b", "c", date(2004, 2, 20), "tel", [Address("Sweden", "Stockholm", "Stockholm", "Torsgatan", "53", "11337")])

p.add_address("pina_colada")

print(p.age)
