question = "3 5"

"""
Delar upp strängen "3 5" vid " "(mellanslag) vilket ger listan ["3", "5"]
"""
question = question.split()
print(question)

"""
Applicerar funktionen int() på varje object i listan ["3", "5"] vilket skapar
ett map-object som "innehåller" elementen 3 och 5. Map-objektet konverteras sedan
till en lista med list() vilket returnerar listan [3, 5]
"""
question = list(map(int, question))
print(question)


def func(x, y):
    return x, y


"""
* (stjärna/asterix) operatorn kan användas innan kollektioner, exempelvis list, dict, tuple, m.m., för att "packa upp"
de till individuella objekt

func(question) == func([3, 5]) -> ger en error då func förväntar sig två argument men bara får ett

func(*question) == func(3, 5) -> ger inte en error då funktionen ges två argument
"""
print(func(*question))
