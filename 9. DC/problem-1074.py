import sys

input = sys.stdin.readline


def Z(N: int, target: set):
    order = 0

    start = (0, 0)
    length = 2 ** N
    step = length // 2
    area = step * step

    while length > 1:

        if length == 2:
            run = True
            for r in range(2):
                for c in range(2):
                    if run:
                        if start[0] + r == target[0] and start[1] + c == target[1]:
                            run = False
                            break
                        order += 1
            break

        if target[0] < start[0] + step and target[1] < start[1] + step:
            pass
        elif target[0] < start[0] + step and target[1] >= start[1] + step:
            start = (start[0], start[1] + step)
            order += area
        elif target[0] >= start[0] + step and target[1] < start[1] + step:
            start = (start[0] + step, start[1])
            order += area * 2
        elif target[0] >= start[0] + step and target[1] >= start[1] + step:
            start = (start[0] + step, start[1] + step)
            order += area * 3

        length = length // 2
        step = step // 2
        area = area // 4

    return order


N, row, column = map(int, input().split())
print(Z(N, (row, column)))
