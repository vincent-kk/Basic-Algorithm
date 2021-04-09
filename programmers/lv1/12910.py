from typing import List


def solution(arr: List[int], divisor: int):
    answer = []
    for element in arr:
        if element % divisor == 0:
            answer.append(element)
    if len(answer) == 0:
        return [-1]
    return sorted(answer)


if __name__ == "__main__":
    i = [20, 5, 9, 7, 10]
    d = 5
    print(solution(i, d))
