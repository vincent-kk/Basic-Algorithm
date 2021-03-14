from collections import Counter


class Solution:
    def numSplits(self, s: str):
        left, right = Counter(), Counter(s)
        good = 0
        for c in s:
            left[c] += 1
            right[c] -= 1
            if right[c] == 0:
                del right[c]
            if len(left) == len(right):
                good += 1
            elif good:
                break

        return good


s = Solution()
i = "acbadbaada"
o = s.numSplits(i)
print(o)