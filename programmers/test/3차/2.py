def solution(n):
    answer = 1
    while n > 1:
        if n % 2:
            n -= 1
            answer += 1
        n = n // 2

    return answer