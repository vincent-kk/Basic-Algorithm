import sys
from typing import List, Tuple
from collections import deque

input = sys.stdin.readline


def solution(
    room: List[List[int]], size: Tuple[int], start: Tuple[int], fires: List[Tuple[int]]
) -> int:
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    R, C = size
    person_queue = deque([start])
    fire_queue = deque(fires)

    for r, c in fires:
        room[r][c] = 3
    r, c = start
    room[r][c] = 2

    time = 1
    while person_queue:
        for _ in range(len(fire_queue)):
            tr, tc = fire_queue.popleft()
            for dr, dc in directions:
                r, c = tr + dr, tc + dc
                if 0 <= r < R and 0 <= c < C:
                    if room[r][c] < 3:
                        room[r][c] = 3
                        fire_queue.append((r, c))

        for _ in range(len(person_queue)):
            tr, tc = person_queue.popleft()
            if tr == 0 or tr == (R - 1) or tc == 0 or tc == (C - 1):
                return time
            for dr, dc in directions:
                r, c = tr + dr, tc + dc
                if 0 <= r < R and 0 <= c < C:
                    if room[r][c] < 2:
                        room[r][c] = 2
                        person_queue.append((r, c))

        time += 1
    return -1


N = int(input())

for _ in range(N):
    C, R = map(int, input().split())
    room = []
    start = (0, 0)
    fires = []
    for r in range(R):
        line = input()[:-1]
        if "@" in line:
            start = (r, line.find("@"))

        if "*" in line:
            fire = 0
            while True:
                fire = line.find("*", fire + 1)
                if fire < 0:
                    break
                fires.append((r, fire))
        line = list(map(lambda e: 4 if e == "#" else 3 if e == "*" else 1, line))
        room.append(line)

    time = solution(room, (R, C), start, fires)
    print(time if time > 0 else "IMPOSSIBLE")
