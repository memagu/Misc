class Drink:
    def __init__(self, sort, alkoholvolym):
        self.sort = sort
        self.alkoholvolym = alkoholvolym

    def blanda_med(self, annan_drink):
        blandad_sort = self.sort[:len(self.sort) // 2] + annan_drink.sort[len(self.sort) // 2:]
        blandad_alkoholvolym = self.alkoholvolym + annan_drink.alkoholvolym
        return Drink(blandad_sort, blandad_alkoholvolym)


mojito = Drink("mojito", 10)
bloodymary = Drink("bloodymary", 15)

ny_drink = mojito.blanda_med(bloodymary)

print(ny_drink.sort)
print(ny_drink.alkoholvolym)