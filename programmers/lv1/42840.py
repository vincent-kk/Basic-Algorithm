from typing import List


def solution(answers: List[int]) -> List[int]:

    users = [
        {"p": [1, 2, 3, 4, 5], "l": 5},
        {"p": [2, 1, 2, 3, 2, 4, 2, 5], "l": 8},
        {"p": [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], "l": 10},
    ]

    result = [0, 0, 0]

    for i, answer in enumerate(answers):
        for j in range(len(result)):
            result[j] += 1 if users[j]["p"][i % users[j]["l"]] == answer else 0

    answer = []
    for i, r in enumerate(result):
        if r == max(result):
            answer.append(i + 1)

    return answer


if __name__ == "__main__":
    i = [1, 2, 3, 4, 5]
    print(solution(i))