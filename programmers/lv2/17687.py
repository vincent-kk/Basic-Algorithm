from typing import List


def getNBaseNumber(base: int, num: int) -> List[str]:
    numbermap = "0123456789ABCDEF"
    answer = []
    while num >= base:
        answer.append(numbermap[num % base])
        num = num // base
    else:
        answer.append(numbermap[num % base])
    answer.reverse()
    return answer


def solution(n, t, m, p):
    this = 0
    left = p - 1
    answer = ""
    while len(answer) < t:
        transed = getNBaseNumber(n, this)
        while left > 0:
            if len(transed) > left:
                break
            else:
                left -= len(transed)
                this += 1
                transed = getNBaseNumber(n, this)

        answer += transed[left]
        left += m

    return answer


if __name__ == "__main__":
    i = 16, 16, 2, 2
    print(solution(*i))
