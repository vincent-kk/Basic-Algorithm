from typing import List


def solution(a: List[int], b: List[int]):
    length = len(a)
    answer = 0
    for i in range(length):
        answer += a[i] * b[i]
    return answer

    # return sum([x*y for x, y in zip(a,b)])


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = [-3, -1, 0, 2]
    print(solution(a, b))
