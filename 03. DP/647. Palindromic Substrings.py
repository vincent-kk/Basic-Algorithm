class Solution:
    def countSubstrings(self, s: str):
        length = len(s) - 1
        conter = 0

        def compair(i, j):
            if i < 0 or i > length:
                return False
            if j < 0 or j > length:
                return False
            return s[i] == s[j]

        for i in range(length + 1):

            size = 0
            while compair(i - size, i + size):
                conter += 1
                size += 1

            size = 0
            while compair(i - size, i + 1 + size):
                conter += 1
                size += 1
        return conter


s = Solution()
i = "abc"
o = s.countSubstrings(i)
print(o)