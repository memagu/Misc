from dataclasses import dataclass


@dataclass()
class Address:
    country: str
    state: str
    city: str
    street: str
    street_number: str
    postal_code: str
