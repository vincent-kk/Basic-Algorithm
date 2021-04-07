from sys import stdin
from typing import Deque
from collections import deque

input = stdin.readline


def solution(N: int):
    cards: Deque = deque(range(1, N + 1))
    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())
    return cards[0]


if __name__ == "__main__":
    N = int(input())
    print(solution(N))