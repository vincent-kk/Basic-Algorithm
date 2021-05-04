import sys

input = sys.stdin.readline


def solution(N: int):
    odd = [1 for _ in range(10)]
    even = [0 for _ in range(10)]
    final = odd

    for n in range(2, N + 1):
        sorce = odd if n % 2 == 0 else even
        target = even if n % 2 == 0 else odd
        target[0] = sorce[0] % 10007
        for i in range(1, 10):
            target[i] = (target[i - 1] % 10007 + sorce[i] % 10007) % 10007
        final = target

    return sum(final) % 10007


N = int(input())
print(solution(N))