numerator = [1, -4, 9, -4, 9]  # x^4 - 4x^3 + 9x^2 - 4x + 8
# numerator = list(map(int, input("Input numerator: ").split()))

numerator_grade = len(numerator) - 1
numerator_for_print = [*numerator][::-1]

denominator = [1, 0, 1]  # x^2 + 1
# denominator = list(map(int, input("Input denominator: ").split()))

denominator_grade = len(denominator) - 1
denominator_for_print = [*denominator][::-1]

result = list(0 for _ in range(numerator_grade + 1))

for i in range(numerator_grade - denominator_grade + 1):
    current_grade = numerator_grade - i
    grade_gap = current_grade - denominator_grade

    multiplier = numerator[i] / denominator[0]

    result[grade_gap] = multiplier

    for j in range(denominator_grade + 1):
        numerator[i + j] -= denominator[j] * multiplier


def polynomial_list_to_string(polynomial, variable='x'):
    polynomial = polynomial[::-1]
    polynomial_grade = len(polynomial) - 1
    polynomial_string = ""
    first = True

    for i, coefficient in enumerate(polynomial):
        if coefficient == 0:
            continue

        if first:
            if i == len(polynomial) - 1:
                polynomial_string += f"{'-' if coefficient < 0 else ''}{abs(coefficient)}"

            elif i == len(polynomial) - 2:
                polynomial_string += f"{'-' if coefficient < 0 else ''}{abs(coefficient) if coefficient != 1 else ''}{variable}"

            else:
                polynomial_string += f"{'-' if coefficient < 0 else ''}{coefficient if abs(coefficient) != 1 else ''}{variable}^{polynomial_grade - i}"
            first = False
            continue

        if i == len(polynomial) - 1 and not first:
            polynomial_string += f"{' + ' if coefficient > 0 else ' - ' if coefficient < 0 else ''}{abs(coefficient)}"
            continue

        if i == len(polynomial) - 2 and not first:
            polynomial_string += f"{' + ' if coefficient > 0 else ' - ' if coefficient < 0 else ''}{abs(coefficient) if coefficient != 1 else ''}{variable}"
            continue

        if not first:
            polynomial_string += f"{' + ' if coefficient > 0 else ' - ' if coefficient < 0 else ''}{abs(coefficient) if abs(coefficient) != 1 else ''}{variable}^{polynomial_grade - i}"

    return polynomial_string


print(f"result = {polynomial_list_to_string(result)}")
if not all(coefficient == 0 for coefficient in numerator):
    print(f"rest = {polynomial_list_to_string(numerator[::-1])}")
