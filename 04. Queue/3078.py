from sys import stdin
from typing import List, Tuple
from collections import defaultdict, deque

input = stdin.readline


def solution(N: int, K: int, students: List[int]):
    friends = defaultdict(deque)
    good_friend = 0
    for student in enumerate(students):
        if student[1] in friends:
            q = friends[student[1]]
            while len(q) > 0:
                if student[0] - q[0][0] > K:
                    q.popleft()
                else:
                    break
            good_friend += len(q)
            q.append(student)
        else:
            friends[student[1]].append(student)

    return good_friend


if __name__ == "__main__":
    N, K = map(int, input().split())
    students = []
    for i in range(N):
        students.append(len(input()[:-1]))
    print(solution(N, K, students))
