import sys

input = sys.stdin.readline


def Z(N: int, target: set):

    if (2 ** N) - 1 < target[0] or (2 ** N) - 1 < target[1]:
        return False
    order = 0
    run = True

    def zTravel(size: int, point: set):
        nonlocal run
        nonlocal order
        if size == 1:
            for r in range(2):
                for c in range(2):
                    if run:
                        if point[0] + r == row and point[1] + c == column:
                            run = False
                            break
                        order += 1
            return

        step = 2 ** (size - 1)
        mid = (point[0] + step, point[1] + step)

        if target[0] < mid[0] and target[1] < mid[1]:
            zTravel(size - 1, point)
        if target[0] < mid[0] and target[1] > mid[1]:
            order += step * step
            zTravel(size - 1, (point[0], point[1] + step))
        if target[0] > mid[0] and target[1] < mid[1]:
            order += step * step * 2
            zTravel(size - 1, (point[0] + step, point[1]))
        if target[0] >= mid[0] and target[1] >= mid[1]:
            order += step * step * 3
            zTravel(size - 1, (point[0] + step, point[1] + step))

    zTravel(N, (0, 0))
    return order


N, row, column = map(int, input().split())
print(Z(N, (row, column)))
