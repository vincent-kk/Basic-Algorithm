
from typing import List
from functools import lru_cache


def fmax(x, y): return x if x > y else y
def fmin(x, y): return x if x < y else y


class Solution:
    def mctFromLeafValues(self, arr: List[int]):
        size = len(arr) - 1

        @lru_cache(maxsize=None)
        def calcMinSubArray(start, end):
            if start == end:
                return 0
            global_minimum = -1
            for target in range(start, end):
                left_max = max(arr[start:target+1])
                right_max = max(arr[target+1:end+1])
                new_node = left_max * right_max

                left_sum = calcMinSubArray(start, target)
                right_sum = calcMinSubArray(target+1, end)
                local_minimum = new_node + left_sum + right_sum

                global_minimum = fmin(global_minimum, local_minimum) if (
                    global_minimum > 0) else local_minimum

            return global_minimum if global_minimum > 0 else 0

        return calcMinSubArray(0, size)


s = Solution()
arr = [6, 2, 4]
o = s.mctFromLeafValues(arr)

print(o)
