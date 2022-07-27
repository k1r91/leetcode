class Solution:

    def reverse_string(self, s: str)  -> str:
        s = list(s)
        s.reverse()
        return ''.join(s)

    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = list(map(lambda x: self.reverse_string(x), s))
        return ' '.join(s)


if __name__ == '__main__':
    Solution().reverseWords("Let's take LeetCode contest")