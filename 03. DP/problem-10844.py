import sys

input = sys.stdin.readline


def solution(N: int):
    odd = [1 for _ in range(10)]
    even = [0 for _ in range(10)]
    odd[0] = 0
    final = odd

    for n in range(2, N + 1):
        sorce = odd if n % 2 == 0 else even
        target = even if n % 2 == 0 else odd

        for i in range(10):
            if i == 0:
                target[i] = sorce[1] % 1000000000
            elif i == 9:
                target[i] = sorce[8] % 1000000000
            else:
                target[i] = (
                    sorce[i - 1] % 1000000000 + sorce[i + 1] % 1000000000
                ) % 1000000000
        final = target

    return sum(final) % 1000000000


N = int(input())
print(solution(N))