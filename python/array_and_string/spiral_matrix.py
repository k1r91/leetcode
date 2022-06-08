from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        walked_points = dict()
        result = list()
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        direction = "right"
        for _ in range(m * n):
            result.append(matrix[i][j])
            walked_points.update({(i, j): True})
            if (j == n - 1 or walked_points.get((i, j + 1)) is not None) and direction == "right":
                direction = "down"
            if (i == m - 1 or walked_points.get((i + 1, j)) is not None) and direction == "down":
                direction = "left"
            if (j == 0 or walked_points.get((i, j - 1)) is not None) and direction == "left":
                direction = "up"
            if (i == 0 or walked_points.get((i - 1, j)) is not None) and direction == "up":
                direction = "right"
            if j < n - 1 and walked_points.get((i, j + 1)) is None and direction == "right":
                j += 1
            elif i < m - 1 and walked_points.get((i + 1, j)) is None and direction == "down":
                i += 1
            elif j > 0 and walked_points.get((i, j - 1)) is None and direction == "left":
                j -= 1
            elif i > 0 and walked_points.get((i - 1, j)) is None and direction == "up":
                i -= 1
        return result


if __name__ == '__main__':
    assert Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [1, 2, 3, 4, 8,
                                                                                                       12,
                                                                                                       16, 15, 14, 13,
                                                                                                       9,
                                                                                                       5, 6, 7, 11, 10]
    assert Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6,
                                                                                     7]
    assert Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
