from typing import List


class Solution:

    # def rotate(self, nums: List[int], k: int) -> None:
    #     if k == 0:
    #         return
    #     nums_length = len(nums)
    #     k = k % nums_length
    #     for _ in range(k):
    #         last = nums[-1]
    #         i = nums_length - 1
    #         while i > 0:
    #             nums[i] = nums[i - 1]
    #             i -= 1
    #         nums[0] = last
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]


if __name__ == '__main__':
    Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
    Solution().rotate([-1, -100, 3, 99], 2)
    # Solution().rotate([-1, -100, 3, 99], 2)
