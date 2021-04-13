def solution(n: int):
    sqrt = n ** (1 / 2)
    if sqrt % 1 == 0:
        return (int(sqrt) + 1) ** 2
    else:
        return -1


if __name__ == "__main__":
    i = 121
    print(solution(i))
