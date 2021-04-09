from typing import List


def solution(strings: List[str], n: int):
    strings.sort()
    answer = sorted(strings, key=lambda s: s[n])
    return answer


if __name__ == "__main__":
    s = ["abce", "abcd", "cdx"]
    n = 2
    print(solution(s, n))
