from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return result

        for i in range(1, numRows - 1):
            append_list = [1, 1]
            for j in range(i):
                append_list.insert(j + 1, sum([result[i][j], result[i][j+1]]))
            result.append(append_list)
        return result


if __name__ == '__main__':
    assert Solution().generate(1) == [[1]]
    assert Solution().generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
