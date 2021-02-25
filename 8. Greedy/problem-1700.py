import sys
from typing import List


input = sys.stdin.readline


def solution(N: int, K: int, tasks: List):

    plusboard = []
    switch = 0

    for i in range(len(tasks)):
        if tasks[i] in plusboard:
            continue
        if len(plusboard) == N:
            target = plusboard[0]
            target_index = tasks[i:].index(target) if (target in tasks[i:]) else K + 1
            for plug in plusboard:
                plug_index = tasks[i:].index(plug) if (plug in tasks[i:]) else K + 1
                if plug_index > K:
                    target = plug
                    break
                if plug_index > target_index:
                    target = plug
                    target_index = plug_index
            plusboard.remove(target)
            switch += 1
        plusboard.append(tasks[i])

    return switch


N, K = map(int, input().split())
tasks = list(map(int, input().split()))

print(solution(N, K, tasks))
