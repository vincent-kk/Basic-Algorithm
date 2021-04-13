def solution(n: int):
    # l = str(n)
    # answer = 0
    # for i in l:
    #     answer += int(i)
    return sum(map(int, str(n)))


if __name__ == "__main__":
    i = 123
    print(solution(i))
