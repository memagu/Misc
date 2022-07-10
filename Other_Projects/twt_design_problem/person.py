from adress import Address
from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Person:
    first_name: str
    middle_name: str
    last_name: str
    date_of_birth: date
    phone_number: str
    addresses: List[Address]

    @property
    def age(self):
        return date.today() - self.date_of_birth

    def add_address(self, address):
        if not isinstance(address, Address):
            raise TypeError
        self.addresses.append(address)

    def remove_address(self, address):
        if not isinstance(address, Address):
            raise TypeError
        self.addresses.remove(address)


