import sys
from typing import List, Tuple

input = sys.stdin.readline


def solution(N: int, strings: List[Tuple[str]]):
    goodword = 0
    for string in strings:
        stack = []
        for ch in string:
            if len(stack) == 0:
                stack.append(ch)
            else:
                if stack[-1] == ch:
                    stack.pop()
                else:
                    stack.append(ch)
        if len(stack) == 0:
            goodword += 1
    return goodword


if __name__ == "__main__":
    N = int(input())
    strings = [tuple(input()[:-1]) for _ in range(N)]
    print(solution(N, strings))
