def solution(x: int, n: int):
    answer = []
    prev = 0
    while len(answer) < n:
        prev += x
        answer.append(prev)

    return answer


if __name__ == "__main__":
    x = 2
    n = 5
    print(solution(x, n))
