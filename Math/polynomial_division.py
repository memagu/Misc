numerator = [1, -4, 9, -4, 8]  # x^4 - 4x^3 + 9x^2 - 4x + 8

numerator_grade = len(numerator) - 1
numerator_for_print = [*numerator][::-1]

denominator = [1, 0, 1]  # x^2 + 1

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
    result = ""
    first = True

    for i, coefficient in enumerate(polynomial):
        if coefficient == 0:
            continue

        if first:
            if i == len(polynomial) - 1:
                result += f"{'-' if coefficient < 0 else ''}{abs(coefficient)}"

            elif i == len(polynomial) - 2:
                result += f"{'-' if coefficient < 0 else ''}{abs(coefficient) if coefficient != 1 else ''}{variable}"

            else:
                result += f"{'-' if coefficient < 0 else ''}{coefficient if abs(coefficient) != 1 else ''}{variable}^{polynomial_grade - i}"
            first = False
            continue

        if i == len(polynomial) - 1 and not first:
            result += f"{' + ' if coefficient > 0 else ' - ' if coefficient < 0 else ''}{abs(coefficient)}"
            continue

        if i == len(polynomial) - 2 and not first:
            result += f"{' + ' if coefficient > 0 else ' - ' if coefficient < 0 else ''}{abs(coefficient) if coefficient != 1 else ''}{variable}"
            continue

        if not first:
            result += f"{' + ' if coefficient > 0 else ' - ' if coefficient < 0 else ''}{abs(coefficient) if abs(coefficient) != 1 else ''}{variable}^{polynomial_grade - i}"

    return result


numerator_out = polynomial_list_to_string(numerator_for_print)
denominator_out = polynomial_list_to_string(denominator_for_print)
result_out = polynomial_list_to_string(result)
rest_out = polynomial_list_to_string(numerator[::-1])

numerator_string_out = "  " + (numerator_out + ((' ' * (9 + len(result_out)) + " " * (
            (len(denominator_out) + 2) // 2 - len(rest_out) // 2) + rest_out) if not all(coefficient == 0 for coefficient in numerator) else ''))

result_string_out = '-' * (len(numerator_out) + 4) + " = " + polynomial_list_to_string(result) + (
    (" | " + '-' * (len(denominator_out) + 4)) if not all(coefficient == 0 for coefficient in numerator) else '')

denominator_string_out = " " * ((len(numerator_out) + 4) // 2 - len(denominator_out) // 2) + denominator_out + ((' ' * (len(numerator_out) + 4 - (((len(numerator_out) + 2) // 2 - len(denominator_out) // 2)) + len(result_out)) + denominator_out) if not all(coefficient == 0 for coefficient in numerator) else '')

print(numerator_string_out)
print(result_string_out)
print(denominator_string_out)
