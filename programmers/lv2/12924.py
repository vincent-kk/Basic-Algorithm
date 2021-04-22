def solution(n):
    dp = [(i * (i - 1)) // 2 for i in range(1, n + 1)]
    l = 0
    r = 1
    answer = 1
    while r < n and l < r:
        pivot = dp[r] - dp[l]
        if pivot > n:
            l += 1
        else:
            if pivot == n:
                answer += 1
            r += 1

    return answer


if __name__ == "__main__":
    n = 15
    print(solution(n))