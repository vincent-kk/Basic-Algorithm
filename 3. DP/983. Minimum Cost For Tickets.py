from typing import List
from functools import cache


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]):
        length = len(days)
        pass_length = len(costs)
        pass_array = [1, 7, 30]

        @cache
        def findMinimumCost(index):
            if index == length:
                return 0
            global_minimum = float("inf")

            for c in range(pass_length):
                end_of_pass = pass_array[c]
                next_index = index

                while days[next_index] < days[index] + end_of_pass:
                    next_index += 1
                    if next_index == length:
                        break

                local_minimum = costs[c] + findMinimumCost(next_index)
                global_minimum = min(global_minimum, local_minimum)
            return global_minimum

        return findMinimumCost(0)


s = Solution()
i1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
i2 = [2, 7, 15]
o = s.mincostTickets(i1, i2)
print(o)