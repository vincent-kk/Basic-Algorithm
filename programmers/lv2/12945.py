def solution(n):
    prev, this = 0, 1
    for _ in range(2, n + 1):
        prev, this = this % 1234567, (this % 1234567 + prev % 1234567) % 1234567
    return this