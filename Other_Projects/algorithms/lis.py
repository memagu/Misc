from typing import Dict, List
import time


# lis = longest increasing sub sequence


def lis_length(nums: List[float]) -> int:
    cache = [1 for _ in range(len(nums))]

    for i in range(len(nums) - 1, -1, -1):
        max_len = 0
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i] and max_len < cache[j]:
                max_len = cache[j]

        cache[i] += max_len

    return max(cache)


def lis(nums: List[float]) -> List[float]:
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
def lis_recursive(nums: List[float]) -> int:
    head = nums[0]
    tail = nums[1::]
    print(tail, lis_recursive(tail) if tail else 0)

    result = 1 + max([0] + [lis_recursive(tail[i::]) for i in range(len(tail)) if tail[i::][0] > head])


    return max(result, 0 if not tail else lis_recursive(tail))
"""


# Longest subseq up to index
def _lis_recursive(nums: List[float], current_index: int, memo: Dict[int, int] = None) -> int:
    if memo is None:
        memo = {0: 1}

    if current_index not in memo:
        memo[current_index] = max([1] + [1 + _lis_recursive(nums, i) for i in range(current_index - 1, -1, -1)
                                         if nums[i] < nums[current_index]])

    return memo[current_index]


def lis_recursive(nums: List[float]) -> int:
    return max([1] + [_lis_recursive(nums, i) for i in range(len(nums))])


def binary_search(arr: List[float], target: float):
    left = 0
    right = len(arr) - 1
    result = float("inf")
    while left <= right:
        center = int((left + right) / 2)
        if arr[center] >= target:
            result = min(result, center)
            right = center - 1
            continue

        left = center + 1

    return result if result != float("inf") else -1


def lis_fast(nums: [List[float]]):
    lis = [nums[0]]

    for i in range(1, len(nums)):
        index_of_smallest_greater = binary_search(lis, nums[i])
        if index_of_smallest_greater == -1:
            lis.append(nums[i])
            continue

        lis[index_of_smallest_greater] = nums[i]

    return len(lis)


"""
Fungerar nästan

def lis_recursive_combinations(nums: List[float], memo: Dict[List[float], List[float]] = None) -> List[List[float]]:
    if memo is None:
        memo = {(): [[]]}

    nums_tuple = tuple(nums)

    if nums_tuple not in memo:
        result = []

        for i, num in enumerate(nums):
            for num_2 in lis_recursive_combinations(nums[i + 1:], memo):
                if not num_2 or num < num_2[0]:
                    result.append([num] + num_2)

        memo[nums_tuple] = result

    print(memo)
    return memo[nums_tuple]


def lis_recursive_combinations_wo_memo(nums: List[float]) -> List[List[float]]:
    if not nums:
        return [[]]

    result = []

    for i, num in enumerate(nums):
        print(nums)
        for num_2 in lis_recursive_combinations_wo_memo(nums[i + 1:]):
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
    # print(lis_length(a))
    # print(lis(a))
    # print(lis_length(b))
    # print(lis(b))

    # print(lis_recursive(a))
    # print(lis_recursive(b))
    # print(lis_recursive(c))
    # print(lis_recursive(e))
    # print(lis_recursive(d))

    # print(lis_recursive_combinations(a))
    # print(lis_recursive_combinations(b))
    # print(lis_recursive_combinations(c))
    # print(lis_recursive_combinations(d))
    # print(lis_recursive_combinations(e))
    # print(lis_recursive_combinations(f))
    # print(lis_recursive_combinations_wo_memo(g))

    print(lis_fast(a))
    print(lis_fast(b))
    print(lis_fast(c))
    print(lis_fast(d))
    print(lis_fast(e))
    print(lis_fast(f))
    print(lis_fast(g))