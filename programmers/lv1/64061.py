from typing import Dict, List
from collections import defaultdict


def solution(board: List[List[int]], moves: List[int]):
    removed = 0
    trans = defaultdict(list)
    basket = list()
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                continue
            trans[j + 1].append(board[i][j])

    for move in moves:
        row = trans[move]
        if len(row) == 0:
            continue
        item = row.pop()
        if len(basket) > 0 and basket[-1] == item:
            basket.pop()
            removed += 2
        else:
            basket.append(item)

    return removed


if __name__ == "__main__":
    i1 = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1],
    ]
    i2 = [1, 5, 3, 5, 1, 2, 1, 4]
    print(solution(i1, i2))
