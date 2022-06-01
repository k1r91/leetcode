from typing import List


class Solution:

    @staticmethod
    def create_border(mat: List[List[int]]) -> List[tuple]:
        border = list()
        for i in range(len(mat[0])):
            border.append((0, i))
        for i in range(1, len(mat)):
            border.append((i, len(mat[0]) - 1))
        return border

    @staticmethod
    def get_diagonal(mat: List[List[int]], elem: int, reverse: bool = False) -> list:
        diagonal = list()
        x, y = elem[0], elem[1]
        while x <= len(mat) - 1 and y >= 0:
            if reverse:
                diagonal.append(mat[x][y])
            else:
                diagonal.insert(0, mat[x][y])
            x += 1
            y -= 1
        return diagonal

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = list()
        for i, elem in enumerate(self.create_border(mat)):
            if i % 2 == 0:
                reverse = False
            else:
                reverse = True
            result += self.get_diagonal(mat, elem, reverse)
        return result


if __name__ == '__main__':
    # assert Solution().findDiagonalOrder([[1, 2, 3, 4], [44, 5, 6, 7], [77, 8, 9, 10]]) == [1, 2, 4, 7, 5, 3, 6, 8, 9]
    assert Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 4, 7, 5, 3, 6, 8, 9]
    # assert Solution().findDiagonalOrder([[1, 2], [3, 4]]) == [1, 2, 3, 4]
