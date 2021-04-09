def solution(n: int):
    answer = 0
    power = 0
    while 3 ** power <= n:
        power += 1
    power -= 1
    num = n
    while num >= 3:
        mod = num % 3
        num = int(num / 3)
        answer += mod * 3 ** power
        power -= 1
    answer += num
    return answer


if __name__ == "__main__":
    i = 10
    print(solution(i))
