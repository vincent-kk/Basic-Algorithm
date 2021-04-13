def solution(n: int):
    answer = ["수" if i % 2 == 0 else "박" for i in range(n)]
    return "".join(answer)


if __name__ == "__main__":
    i = 3
    print(solution(i))
