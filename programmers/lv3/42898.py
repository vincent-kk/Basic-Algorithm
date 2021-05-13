import collections
from typing import List
from collections import deque


def solution(m: int, n: int, puddles: List[List[int]]) -> int:
    """
    비가 와서 경로의 일부가 물에 잡겼다
    입력된 칸은 물에 잠긴 칸으로 그 길로는 갈 수 없다
    시작지점은 {0,0}, 도착 지점은 {n,m} 이다

    Args:
        m (int): 지도의 가로 길이(C)
        n (int): 지도의 세로 길이(R)
        puddles (List[List[int]]): 지나갈 수 없는 칸

    Returns:
        int: [description]
    """
    cache = [[1] * m for _ in range(n)]
    for c, r in puddles:
        cache[r - 1][c - 1] = 0

    for r in range(n):
        for c in range(m):
            if r == 0:
                if c == 0:
                    continue
                if cache[r][c - 1] == 0:
                    cache[r][c] = 0
                continue
            if c == 0:
                if r == 0:
                    continue
                if cache[r - 1][c] == 0:
                    cache[r][c] = 0
                continue
            if cache[r][c] > 0:
                cache[r][c] = (
                    cache[r][c - 1] % 1000000007 + cache[r - 1][c] % 1000000007
                ) % 1000000007

    return cache[n - 1][m - 1]


if __name__ == "__main__":
    m, n, p = 4, 3, [[2, 2]]
    print(solution(m, n, p))
