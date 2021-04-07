from sys import stdin
from typing import List
from collections import deque

input = stdin.readline


def solution(p: List[str], n: int, array: List[int]):
    revers = False
    array_data = deque(array)
    for op in p:
        if op == "R":
            revers = not revers
        if op == "D":
            if len(array_data) == 0:
                return "error"
            if revers:
                array_data.pop()
            else:
                array_data.popleft()
    if len(array_data) == 0:
        return "[]"
    if revers:
        array_data.reverse()
    return "[" + ",".join(map(str, array_data)) + "]"


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        p = list(input()[:-1])
        n = int(input())
        raw = input()[1:-2]
        if len(raw) == 0:
            array = []
        else:
            array = list(map(int, raw.split(",")))
        print(solution(p, n, array))
