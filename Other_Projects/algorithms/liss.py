from typing import Dict, List
import time


# liss = longest increasing sub sequence


def liss_length(nums: List[float]) -> int:
    counts = [1 for _ in range(len(nums))]

    for i in range(len(nums) - 1, -1, -1):
        max_len = 0
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i] and max_len < counts[j]:
                max_len = counts[j]

        counts[i] += max_len

    return max(counts)


def liss(nums: List[float]) -> List[float]:
    counts = [1 for _ in range(len(nums))]
    longest_sequence = []

    for i in range(len(nums) - 1, -1, -1):
        max_len = 0
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i] and max_len < counts[j]:
                max_len = counts[j]

        if max(counts) < max_len + 1:
            if not len(longest_sequence):
                longest_sequence.append(nums[i + 1])
            longest_sequence.append(nums[i])

        counts[i] += max_len

    return (longest_sequence or [nums[0]])[::-1]


"""
def liss_recursive(nums: List[float]) -> int:
    head = nums[0]
    tail = nums[1::]
    print(tail, liss_recursive(tail) if tail else 0)

    result = 1 + max([0] + [liss_recursive(tail[i::]) for i in range(len(tail)) if tail[i::][0] > head])


    return max(result, 0 if not tail else liss_recursive(tail))
"""


# Longest subseq up to index
def _liss_recursive(nums: List[float], current_index: int, memo: Dict[int, int] = None) -> int:
    if memo is None:
        memo = {0: 1}

    if current_index not in memo:
        memo[current_index] = max([1] + [1 + _liss_recursive(nums, i) for i in range(current_index - 1, -1, -1)
                                         if nums[i] < nums[current_index]])

    return memo[current_index]


def liss_recursive(nums: List[float]) -> int:
    return max([1] + [_liss_recursive(nums, i) for i in range(len(nums))])


"""
Fungerar nästan

def liss_recursive_combinations(nums: List[float], memo: Dict[List[float], List[float]] = None) -> List[List[float]]:
    if memo is None:
        memo = {(): [[]]}

    nums_tuple = tuple(nums)

    if nums_tuple not in memo:
        result = []

        for i, num in enumerate(nums):
            for num_2 in liss_recursive_combinations(nums[i + 1:], memo):
                if not num_2 or num < num_2[0]:
                    result.append([num] + num_2)

        memo[nums_tuple] = result

    print(memo)
    return memo[nums_tuple]


def liss_recursive_combinations_wo_memo(nums: List[float]) -> List[List[float]]:
    if not nums:
        return [[]]

    result = []

    for i, num in enumerate(nums):
        print(nums)
        for num_2 in liss_recursive_combinations_wo_memo(nums[i + 1:]):
            if not num_2 or num < num_2[0]:
                result.append([num] + num_2)

    return result
"""


if __name__ == "__main__":
    a = [10, 9, 2, 5, 3, 7, 101, 18]  # 4
    b = [7, 7, 7, 7, 7, 7]  # 1
    c = [1, 2, 4, 3]  # 3
    d = [4, 10, 4, 3, 8, 9]  # 3
    e = [4, 3, 8, 9]  # 3
    f = [0, 1, 0, 3, 2, 3]  # 4
    g = [1, 3, 6, 7, 9, 4, 10, 5, 6]  # 6
    # print(liss_length(a))
    # print(liss(a))
    # print(liss_length(b))
    # print(liss(b))

    # print(liss_recursive(a))
    # print(liss_recursive(b))
    # print(liss_recursive(c))
    # print(liss_recursive(e))
    # print(liss_recursive(d))

    # print(liss_recursive_combinations(a))
    # print(liss_recursive_combinations(b))
    # print(liss_recursive_combinations(c))
    # print(liss_recursive_combinations(d))
    # print(liss_recursive_combinations(e))
    # print(liss_recursive_combinations(f))
    print(liss_recursive_combinations_wo_memo(g))
