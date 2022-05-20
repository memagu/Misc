numerator = [1, -4, 9, -4, 9]  # x^4 - 4x^3 + 9x^2 - 4x + 8

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


print(f"result = {result[::-1]}")
if not all(coefficient == 0 for coefficient in numerator):
    print(f"rest = {numerator}")
