from typing import List
import copy


def solution(triangle: List[List[int]]) -> int:
    """
    삼각형의 꼭대기[0,0]에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우
    가장 큰 하강 경로 찾기 문제
    아래로 이동하는 경우에는, 대각선 방향으로 한칸, 오른쪽이나 왼쪽으로 이동

    Args:
        triangle (List[List[int]]): 삼각형을 이루는 배열
        7
        3 8
        8 1 0
        2 7 4 4
        4 5 2 6 5

    Returns:
        int: 가장 큰 값을 가지는 하강경로
    """
    H = len(triangle)

    for h in range(1, H):
        for w in range(h + 1):
            triangle[h][w] = (
                max(triangle[h - 1][max(w - 1, 0)], triangle[h - 1][min(w, h - 1)])
                + triangle[h][w]
            )
    return max(triangle[-1])


if __name__ == "__main__":
    t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(t))