class Solution:
    def longestPalindrome(self, s: str):

        def compairChar(s, i, j, limt):
            if i < 0 or i > limt:
                return False
            if j > limt or j < 0:
                return False
            return s[i] == s[j]

        start = 0
        end = 0
        limt = len(s)-1
        for i in range(len(s)):
            if(compairChar(s, i-1, i, limt)):
                subStart = i-1
                subEnd = i
                n = subStart - 1
                m = subEnd + 1
                while compairChar(s, n, m, limt):
                    subStart = n
                    subEnd = m
                    n -= 1
                    m += 1
                if end - start < subEnd - subStart:
                    start, end = subStart, subEnd

            if(compairChar(s, i-1, i+1, limt)):
                subStart = i-1
                subEnd = i+1
                n = subStart - 1
                m = subEnd + 1
                while compairChar(s, n, m, limt):
                    subStart = n
                    subEnd = m
                    n -= 1
                    m += 1
                if end - start < subEnd - subStart:
                    start, end = subStart, subEnd

        return s[start: end+1]


s = Solution()
i = 'ac'
print(s.longestPalindrome(i))
