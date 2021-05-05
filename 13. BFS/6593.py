import sys
from typing import List, Tuple
from collections import deque

input = sys.stdin.readline


def solution(
    building: List[List[List[int]]],
    size: Tuple[int],
    start: Tuple[int],
    end: Tuple[int],
) -> int:
    directions = [(0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    queue = deque([(*start, 1)])
    while queue:
        tl, tr, tc, time = queue.popleft()
        for dl, dr, dc in directions:
            l, r, c = tl + dl, tr + dr, tc + dc
            if (l, r, c) == end:
                return time
            if 0 <= l < size[0] and 0 <= r < size[1] and 0 <= c < size[2]:
                if building[l][r][c]:
                    building[l][r][c] = 0
                    queue.append((l, r, c, time + 1))
    return -1


while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break
    building = []
    start = (0, 0, 0)
    end = (0, 0, 0)

    for f in range(L):
        floor = []
        for r in range(R):
            line = list(input()[:-1])
            if "S" in line:
                start = (f, r, line.index("S"))
            if "E" in line:
                end = (f, r, line.index("E"))
            line = list(map(lambda e: 0 if e == "#" else 1, line))
            floor.append(line)
        building.append(floor)
        input()

    time = solution(building, (L, R, C), start, end)
    print(f"Escaped in {time} minute(s)." if time > 0 else "Trapped!")
