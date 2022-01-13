function = [char for char in input() if char != " "]
independent_variable = function[2]
expression = function[5:]
print(function)
print(independent_variable)
print(expression)

values = []
operations = []

temp = ""

for element in expression:
    if 47 < ord(element) < 58:
        temp += element
    if element == independent_variable
    else:
        values.append(int(temp))
        operations.append(element)

print(values)
print(operations)
