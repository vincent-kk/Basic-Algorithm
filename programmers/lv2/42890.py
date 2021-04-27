from typing import List
from collections import Counter, defaultdict
from itertools import combinations


def solution(r: List[List[str]]) -> int:
    row = len(r)
    calumn = len(r[0])
    relations = defaultdict(list)
    r = zip(*r)

    for k, data in enumerate(r):
        relations[k] = data

    answer = 0
    candidates = set(relations.keys())
    for i in range(1, calumn + 1):
        if len(candidates) < i:
            break
        cases = combinations(candidates, i)
        removed = set()
        for case in cases:
            keys = [tuple([relations[c][i] for c in case]) for i in range(row)]
            count = Counter(keys)
            if all([count[k] == 1 for k in count.keys()]):
                answer += 1
                removed |= set(case)
        candidates -= removed

    return answer


if __name__ == "__main__":
    i = [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"],
    ]
    print(solution(i))