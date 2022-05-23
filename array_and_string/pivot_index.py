from typing import List


def pivot_index(nums: List[int]) -> int:
    left_sum = 0
    right_sum = sum(nums[1:])
    for idx in range(len(nums)):
        if left_sum == right_sum:
            return idx
        try:
            left_sum += nums[idx]
            right_sum -= nums[idx + 1]
        except IndexError:
            continue
    return -1


assert pivot_index([1, 7, 3, 6, 5, 6]) == 3
assert pivot_index([1, 2, 3]) == -1
assert pivot_index([2, 1, -1]) == 0
assert pivot_index([-1, -1, 0, 1, 1, 0]) == 5
