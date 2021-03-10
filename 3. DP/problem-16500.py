import sys
from typing import List
from functools import cache

input = sys.stdin.readline


def solution(target: str, words: List[str]):
    if target == "":
        return target in words

    @cache
    def run(s):
        if s == "":
            return True
        limit = len(s)
        flag = False
        for word in words:
            l = len(word)
            if l > limit:
                continue
            if s[:l] == word:
                flag |= run(s[l:])
        return flag

    return 1 if run(target) else 0


target = input()[:-1]
N = int(input())
words = [input()[:-1] for _ in range(N)]
print(solution(target, words))