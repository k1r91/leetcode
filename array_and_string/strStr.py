class Solution:

    def strStrOld(self, haystack: str, needle: str) -> int:
        c = len(needle)
        z = len(haystack)
        if not needle:
            return 0
        for i in range(z):
            if haystack[i: i + c] == needle:
                return i
        return -1


if __name__ == '__main__':
    assert Solution().strStr("mississippi", "issip") == 4
    # assert Solution().strStr("abc", "c") == 2
    # assert Solution().strStr("a", "a") == 0
    # assert Solution().strStr("hello", "ll") == 2
    # assert Solution().strStr("aaaaa", "bba") == -1
    # assert Solution().strStr("asd", "") == 0
