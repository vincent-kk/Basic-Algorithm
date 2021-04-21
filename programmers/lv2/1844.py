from typing import List
from collections import deque


def solution(maps: List[List[int]]) -> int:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    row, calumn = len(maps), len(maps[0])

    # move count를 함께 저장한다는 것
    start = (0, 0, 1)
    goal = (row - 1, calumn - 1)

    queue = deque([start])
    while queue:
        r, c, move = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) == goal:
                return move + 1
            if 0 <= nr < row and 0 <= nc < calumn and maps[nr][nc]:
                # 되돌아갈 수 없게 0으로 바꿔버린다는 것
                maps[nr][nc] = 0
                queue.append((nr, nc, move + 1))
    return -1


if __name__ == "__main__":
    m = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
    ]
    print(solution(m))
