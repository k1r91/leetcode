from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_index = 0
        i = 0
        nums_length = len(nums)
        while i < nums_length:
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1
            i += 1


if __name__ == '__main__':
    print(Solution().moveZeroes([0, 1, 0, 3, 12]))
