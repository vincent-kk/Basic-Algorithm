def solution(n: int):
    answer = 0
    i = 1
    while i * i < n + 1:
        if n % i == 0:
            if i == n // i:
                answer += i
            else:
                answer += i + n // i
        i += 1
    return answer


if __name__ == "__main__":
    i = 25
    print(solution(i))
