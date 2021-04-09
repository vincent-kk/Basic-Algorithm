def solution(s: str):
    length = len(s)
    mid = int(length / 2)
    if length % 2 == 1:
        return s[mid]
    else:
        return s[mid - 1 : mid + 1]


if __name__ == "__main__":
    i = "qwer"
    print(solution(i))
