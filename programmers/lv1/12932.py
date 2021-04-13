def solution(n: int):
    return list(map(int, reversed(str(n))))


if __name__ == "__main__":
    i = 12345
    print(solution(i))