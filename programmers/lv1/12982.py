from typing import List


def solution(d: List[int], budget: int):
    answer = 0
    sortD = sorted(d)
    for s in sortD:
        if budget - s < 0:
            break
        budget -= s
        answer += 1
    return answer
    # d.sort()
    # while budget < sum(d):
    #     d.pop()
    # return len(d)


if __name__ == "__main__":
    i = [1, 3, 2, 5, 4]
    b = 9
    print(solution(i, b))
