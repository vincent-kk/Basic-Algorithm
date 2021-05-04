import sys
import collections
from typing import List

input = sys.stdin.readline


def solution(N: int, cards: List[int]):
    cache = collections.defaultdict(int)
    cards = [0] + cards
    size = len(cards)
    cache[1] = cards[1]

    for n in range(2, N + 1):
        local_max = 0
        for num in range(1, n + 1 if n + 1 < size else size):
            local_max = (
                local_max
                if local_max > (cache[n - num] + cards[num])
                else cache[n - num] + cards[num]
            )
        cache[n] = local_max

    return cache[N]


N = int(input())
cards = list(map(int, input().split()))

print(solution(N, cards))
