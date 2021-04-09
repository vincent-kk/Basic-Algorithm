def solution(a: int, b: int):
    mid = (a + b) / 2
    length = abs(a - b) + 1

    return int(mid * length)


if __name__ == "__main__":
    a = 5
    b = 3
    print(solution(a, b))
