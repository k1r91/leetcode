from typing import List


class Solution:
    def minSubArrayLen(self, s, nums):
        tmp_sum = left = 0
        ans = len(nums) + 1
        for right, n in enumerate(nums):
            print(tmp_sum, left)
            tmp_sum += n
            while tmp_sum >= s:
                print(tmp_sum, left, right)
                ans = min(ans, right - left + 1)
                tmp_sum -= nums[left]
                left += 1
        return ans if ans <= len(nums) else 0


if __name__ == '__main__':
    assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    # assert Solution().minSubArrayLen(4, [1, 4, 4]) == 1
    # assert Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
