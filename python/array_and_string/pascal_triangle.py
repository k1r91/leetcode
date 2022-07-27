from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[List[int]]:
        result = [[1], [1, 1]]
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        for i in range(1, rowIndex):
            append_list = [1, 1]
            for j in range(i):
                append_list.insert(j + 1, sum([result[i][j], result[i][j + 1]]))
            result.append(append_list)
        return result[-1]


if __name__ == '__main__':
    assert Solution().getRow(3) == [1, 3, 3, 1]
