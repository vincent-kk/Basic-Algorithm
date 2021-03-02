import sys
from typing import List

input = sys.stdin.readline


def quadTree(N: int, image: List[List]):
    def quad(size: int, pr: int, pc: int):
        if size == 1:
            return image[pr][pc]

        global_number = image[pr][pc]
        for r in range(pr, pr + size):
            for c in range(pc, pc + size):
                if global_number != image[r][c]:
                    global_number = None
                    break
            if global_number == None:
                break

        if global_number == None:
            step = size // 2
            lt, rt, lb, rb = (
                quad(step, pr, pc),
                quad(step, pr, pc + step),
                quad(step, pr + step, pc),
                quad(step, pr + step, pc + step),
            )
            return f"({lt}{rt}{lb}{rb})"
        else:
            return global_number

    return quad(N, 0, 0)


N = int(input())
image = []
for _ in range(N):
    row = input()[:-1]
    pixel_row = []
    for pixel in row:
        pixel_row.append(int(pixel))
    image.append(pixel_row)
print(quadTree(N, image))
