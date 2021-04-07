from typing import List


def solution(numbers: List[int]):
    length = len(numbers)
    answer = []
    for i in range(length):
        for j in range(i + 1, length):
            temp = numbers[i] + numbers[j]
            if temp not in answer:
                answer.append(temp)
    return sorted(answer)


if __name__ == "__main__":
    i = [2, 1, 3, 4, 1]
    print(solution(i))