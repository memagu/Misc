from typing import Iterable


def kadane(nums: Iterable[float]) -> float:
    max_sum = current_sum = 0
    for num in nums:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == '__main__':
    print(kadane([1, 1, -1, 1, 1]))
    print(kadane([1, -3, 2, 5, -11, 6]))

