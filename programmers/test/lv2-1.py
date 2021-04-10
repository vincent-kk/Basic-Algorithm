from typing import List


def solution(board: List[List[int]]):
    row, cal = len(board), len(board[0])
    dp = board[:][:]
    global_max = 0
    for i in range(row):
        for j in range(cal):
            if i == 0 or j == 0:
                global_max = max(global_max, dp[i][j])
                continue
            if board[i][j] == 1:
                r1 = dp[i - 1][j - 1]
                r2 = dp[i - 1][j]
                r3 = dp[i][j - 1]
                if r1 > 0 and r2 > 0 and r3 > 0:
                    dp[i][j] = min(r1, r2, r3) + 1
                global_max = max(global_max, dp[i][j])

    return global_max ** 2


if __name__ == "__main__":
    i = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
    print(solution(i))
