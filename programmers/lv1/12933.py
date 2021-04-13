def solution(n: int):
    return int("".join(sorted(str(n), reverse=True)))


if __name__ == "__main__":
    i = 118372
    print(solution(i))
