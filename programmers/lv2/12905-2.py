from typing import List


def solution(board: List[List[int]]) -> int:
    """
    입력된 2차원 배열에서 가장 큰 1로 된 정사각형을 구하라

    Args:
        board (List[List[int]]): 각각의 원소가 1이나 0으로 되어 있는 2차원 배열

    Returns:
        int: 가장 큰 정사각형의 넓이
    """
    row, calumn = len(board), len(board[0])
    global_max = 0
    for i in range(row):
        for j in range(calumn):
            if not (i and j):
                global_max = board[i][j] if board[i][j] > global_max else global_max
                continue
            if board[i][j]:
                near = [board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]]
                board[i][j] = min(near) + 1
                global_max = board[i][j] if board[i][j] > global_max else global_max
    return global_max * global_max


if __name__ == "__main__":
    i = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
    print(solution(i))
