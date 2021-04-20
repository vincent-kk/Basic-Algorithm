from typing import List
from collections import Counter
from itertools import combinations


def solution(orders: List[str], courses: List[int]) -> List[str]:
    answer = []
    for c in courses:
        order = []
        for o in orders:
            if c > len(o):
                continue
            order += combinations(sorted(o), c)
        c = Counter(order)
        if not c:
            continue
        m = max(c.values())
        if m < 2:
            continue
        for course in filter(lambda x: c[x] == m, c.keys()):
            answer.append(course)
        answer.sort()
    return answer


"""
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]
"""

if __name__ == "__main__":
    i = ["XYZ", "XWY", "WXA"]
    r = [2, 3, 4]
    print(solution(i, r))
