from typing import List

# 배열 회전 방법 기억해두자
def rotaeKey(arr):
    return list(zip(*arr[::-1]))


def check(key, lock, x, y):
    key_l = len(key)
    lock_l = len(lock)
    board_l = lock_l * 3
    board = [[0 for c in range(board_l)] for r in range(board_l)]

    start = lock_l - 1
    end = start + lock_l

    for r in range(lock_l):
        for c in range(lock_l):
            board[start + r][start + c] += lock[r][c]

    for r in range(key_l):
        for c in range(key_l):
            board[x + r][y + c] += key[r][c]

    for r in range(start, end):
        for c in range(start, end):
            if board[r][c] != 1:
                return False

    return True


def solution(key: List[List[int]], lock: List[List[int]]) -> bool:
    l = len(lock)
    for _ in range(4):
        for x in range((l * 2) - 1):
            for y in range((l * 2) - 1):
                if check(key, lock, x, y):
                    return True
        key = rotaeKey(key)
    return False


if __name__ == "__main__":
    l = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    k = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    print(solution(k, l))