from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        count_consecutives = 0
        max_count_consecutives = 0
        while i < len(nums):
            if nums[i] == 1 and i == 0:
                count_consecutives += 1
            elif nums[i] == 1 and nums[i-1] == 1:
                count_consecutives += 1
            elif nums[i] == 1 and nums[i-1] != 1:
                count_consecutives = 1
            else:
                count_consecutives = 0
            if count_consecutives > max_count_consecutives:
                max_count_consecutives = count_consecutives
            i += 1
        return max_count_consecutives


if __name__ == '__main__':
    assert Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
    assert Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
