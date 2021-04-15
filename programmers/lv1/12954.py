from typing import List


def solution(x: int, n: int) -> List[int]:
    if x == 0:
        return [x] * n
    return list(range(x, x * (n + 1), x))


if __name__ == "__main__":
    x = -10000000
    n = 1000

    print(solution(x, n))
