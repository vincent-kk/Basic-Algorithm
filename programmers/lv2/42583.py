from typing import List, Tuple
from collections import defaultdict, deque


def solution(bridge_length: int, weight: int, truck_weights: List[int]) -> int:
    time = 0
    timestamp = defaultdict(int)
    on_bridge = 0
    length = len(truck_weights)
    i, j = 0, 0

    while timestamp[length - 1] < bridge_length:
        for t in range(i, j):
            timestamp[t] += 1
        if timestamp[i] == bridge_length:
            on_bridge -= truck_weights[i]
            i += 1
        if j < length:
            if on_bridge + truck_weights[j] <= weight:
                on_bridge += truck_weights[j]
                j += 1
        time += 1

    return time


if __name__ == "__main__":
    bl = 100
    w = 100
    tw = [10]
    print(solution(bl, w, tw))
