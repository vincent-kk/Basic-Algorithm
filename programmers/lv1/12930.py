def solution(s: str):
    words = s.split(" ")
    answer = []
    for word in words:
        chars = list(word)
        for i in range(len(chars)):
            if i % 2 == 0:
                chars[i] = chars[i].upper()
            else:
                chars[i] = chars[i].lower()
        answer.append("".join(chars))

    return " ".join(answer)
    # return " ".join(
    #     map(
    #         lambda x: "".join(
    #             [a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]
    #         ),
    #         s.split(" "),
    #     )
    # )


if __name__ == "__main__":
    i = "try hello   world"
    print(solution(i))