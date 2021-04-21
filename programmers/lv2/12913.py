from typing import List
from functools import lru_cache


def solution(lands: List[List[int]]) -> int:
    """
    땅따먹기 게임
    N행 4열로 구성되어 있음
    0행부터 땅을 밟으며 내려옴
    1개 행당 1개 셀만 밟을 수 있음
    같은 열을 연속해서 밟을 수 없음

    Args:
        land (List[List[int]]): N행 4열로 구성된 2차원 배열

    Returns:
        int: 0번부터 N-1번까지 순회하였을때, 지나친 땅의 최대값
    """
    row, calumn = len(lands), len(lands[0])

    # dp = [[0 for _ in range(calumn)] for _ in range(row)]
    dp = ([0] * calumn, lands[0][:])

    for n in range(1, row):
        for i in range(calumn):
            prev_max = -1
            for j in range(calumn):
                if i == j:
                    continue
                prev_max = max(prev_max, dp[n % 2][j])
            dp[(n + 1) % 2][i] = lands[n][i] + prev_max

    return max(dp[row % 2])

    # @lru_cache(maxsize=None)
    # def dominate(r, c):
    #     if r == row - 1:
    #         return land[r][c]

    #     local_max = -1
    #     for i in range(calumn):
    #         if i == c:
    #             continue
    #         local_max = max(dominate(r + 1, i), local_max)
    #     return land[r][c] + local_max

    # global_max = -1
    # for i in range(calumn):
    #     global_max = max(dominate(0, i), global_max)

    # return global_max


if __name__ == "__main__":
    i = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
    print(solution(i))