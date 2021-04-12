def solution(s: str):
    return "".join(sorted(s, reverse=True))


if __name__ == "__main__":
    i = "Zbcdefg"
    print(solution(i))