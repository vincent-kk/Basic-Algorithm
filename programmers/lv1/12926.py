def solution(s: str, n: int):
    answer = []
    for ch in s:
        if ch.isspace():
            answer.append(ch)
            continue
        asc = ord(ch)
        if 65 <= asc <= 90:
            ch = chr((asc + n - 65) % 26 + 65)
        elif 97 <= asc <= 122:
            ch = chr((asc + n - 97) % 26 + 97)
        answer.append(ch)
    return "".join(answer)

    # s = list(s)
    # for i in range(len(s)):
    #     if s[i].isupper():
    #         s[i] = chr((ord(s[i]) - ord("A") + n) % 26 + ord("A"))
    #     elif s[i].islower():
    #         s[i] = chr((ord(s[i]) - ord("a") + n) % 26 + ord("a"))

    # return "".join(s)


if __name__ == "__main__":
    s = "a B z"
    i = 4
    print(solution(s, i))
