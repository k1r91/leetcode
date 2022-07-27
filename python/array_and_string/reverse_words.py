class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        return ' '.join(s)


if __name__ == '__main__':
    Solution().reverseWords('the sky is blue')