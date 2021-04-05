import sys
from typing import List

input = sys.stdin.readline


def solution(input_data: List[str]):
    stack = []
    for i in input_data:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return len(stack) == 0


N = int(input())

for _ in range(N):
    input_data = list(input().strip())
    print("YES" if solution(input_data) else "NO")
