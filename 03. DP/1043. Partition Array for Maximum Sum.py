from typing import List
from functools import lru_cache


def fmax(x, y): return x if x > y else y
def fmin(x, y): return x if x < y else y


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int):
        size = len(arr)

        @lru_cache(None)
        def findMaxSum(start):
            # Base: 수열의 끝에 도달하면 종료
            if start == size:
                return 0

            local_max = 0
            max_sum = 0

            for end in range(start, fmin(size, start+k)):
                # 현재 부분수열 중에서 가장 큰 요소를 선택
                local_max = fmax(local_max, arr[end])
                # 현재 경우([start,end]의 부분수열인 경우)의 최대값 계산
                # findMaxSum(end+1): 부분수열의 바로 뒤에서 계산한 최대값
                local_sum = local_max * (end-start+1) + findMaxSum(end+1)
                # 이전 값과 새 값 중에서 더 큰 값을 기록
                max_sum = fmax(max_sum, local_sum)
            return max_sum

        return findMaxSum(0)


s = Solution()
arr = [15, 2, 14, 13, 7, 9, 6, 5, 3, 8]
k = 4
o = s.maxSumAfterPartitioning(arr, k)

print(o)
