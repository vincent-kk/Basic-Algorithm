from typing import List
from functools import lru_cache


def calcArea(s, e, h):
    return (e - s) * min(h[e], h[s])


class Solution:
    def maxArea(self, height: List[int]):
        length = len(height) - 1

        @lru_cache(None)
        def findMaxArea(start, end):
            if end <= start or start < 0 or end > length:
                return 0

            this_area = calcArea(start, end, height)
            prev_area = 0
            if height[end] > height[start]:
                prev_area = findMaxArea(start + 1, end)
            elif height[end] < height[start]:
                prev_area = findMaxArea(start, end - 1)
            else:
                prev_area = max(
                    findMaxArea(start + 1, end), findMaxArea(start, end - 1)
                )
            return max(this_area, prev_area)

        return findMaxArea(0, length)


s = Solution()
i = [4, 3, 2, 1, 4]
o = s.maxArea(i)

print(o)