import sys

input = sys.stdin.readline


def countTile(N: int):
    end_with_tile1x2 = 1
    end_with_tile2x1 = 1
    if N < 2:
        return end_with_tile1x2
    for _ in range(N - 2):
        end_with_tile1x2, end_with_tile2x1 = (
            (end_with_tile1x2 % 10007 + end_with_tile2x1 % 10007) % 10007,
            end_with_tile1x2,
        )
    return (end_with_tile1x2 % 10007 + end_with_tile2x1 % 10007) % 10007


i = int(input())
print(countTile(i))
