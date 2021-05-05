import sys
from typing import List, Tuple
from collections import deque

input = sys.stdin.readline


def solution(room: List[List[int]], size: Tuple[int], start: Tuple[int]):
    person = deque([start])

    pass


N = int(input())

for _ in range(N):
    R, C = map(int, input().split())
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
        line = list(map(lambda e: 0 if e == "#" else -1 if e == "*" else 1, line))
        room.append(line)
    time = solution(room, (R, C), start)
