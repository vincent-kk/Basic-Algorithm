from collections import deque


def solution(n: int) -> str:
    dq = deque()
    n -= 1
    while n >= 3:
        dq.appendleft(str(2 ** (n % 3)))
        n = (n // 3) - 1

    dq.appendleft(str(2 ** (n % 3)))

    return "".join(dq)


if __name__ == "__main__":
    i = 3
    print(solution(i))