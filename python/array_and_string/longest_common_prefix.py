from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        # max_i = min(list(map(len, strs)))
        for i in range(len(strs[0])):
            try:
                sym = strs[0][i]
                for s in strs:
                    if s[i] != sym:
                        return prefix
                prefix = ''.join([prefix, sym])
            except IndexError:
                return prefix
        return prefix


if __name__ == '__main__':
    Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ''
    Solution().longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
