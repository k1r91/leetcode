from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s = s[::-1] # actually the fastest
        # s.reverse()
        # below native
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    assert Solution().reverseString(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
