def fmax(x, y): return x if x > y else y
def fmin(x, y): return x if x < y else y


class Solution(object):
    def lengthOfLongestSubstring(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        start = -1
        subSum = -1
        answer = 0
        for i in range(len(s)):
            if start < 0:
                subSum = 1
                start = i

            elif s[i] in s[start:i]:
                start = start + s[start:i].find(s[i]) + 1
                subSum = i - start + 1
            else:
                subSum += 1
            answer = fmax(answer, subSum)
        return answer


s = Solution()
i = 'dvdf'
print(s.lengthOfLongestSubstring(i))
