from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        if j == 0 and nums[0] == val:
            return 0
        while i < len(nums) and j >= i:
            if nums[j] == val:
                nums[j] = '_'
                j -= 1
                continue
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                nums[j] = '_'
                j -= 1
            i += 1
        return i, nums


if __name__ == '__main__':
    assert Solution().removeElement([3, 2, 2, 3], 3) == (2, [2, 2, '_', '_'])
    assert Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == (5, [0, 1, 4, 0, 3, '_', '_', '_'])
    assert Solution().removeElement([3, 3], 3) == (0, ['_', '_'])
