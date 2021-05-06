import sys
from typing import List

input = sys.stdin.readline


def solution(L: int, C: int, characters: List[str]):
    characters.sort()
    answers = []
    vowels = set(["a", "e", "i", "o", "u"])

    def dfs(index, length, pw, v):
        if length == L and v > 0:
            nonlocal answers
            answers.append(pw)
            return

        for i in range(index + 1, C):
            dfs(i, length, pw, v)
            v += 1 if characters[index] in vowels else 0
            dfs(i, length + 1, pw + characters[index], v)

    dfs(0, 0, "", 0)
    return answers


L, C = map(int, input().split())
characters = list(input()[:-1].split())

print(solution(L, C, characters))
