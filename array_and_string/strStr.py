class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i, sym in enumerate(haystack):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    assert Solution().strStr("hello", "ll") == 2
    assert Solution().strStr("aaaaa", "bba") == -1
    assert Solution().strStr("asd", "") == 0
