from typing import List


def dominant_index(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    index_max = 0
    for i, elem in enumerate(nums):
        if nums[index_max] < nums[i]:
            index_max = i
    for i, elem in enumerate(nums):
        if elem != nums[index_max] and elem * 2 > nums[index_max]:
            return -1
    return index_max


assert dominant_index([3, 6, 1, 0]) == 1

assert dominant_index([1]) == 0

assert dominant_index([1, 2, 3, 4]) == -1
