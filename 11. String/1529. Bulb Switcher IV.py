class Solution:
    def minFlips(self, target: str):
        flips = 0
        state = "0"
        for ch in target:
            if ch != state:
                state = ch
                flips += 1
        return flips


s = Solution()
i = "001011101"
o = s.minFlips(i)
print(o)