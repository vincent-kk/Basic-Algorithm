from collections import Counter


def solution(s: str):
    counter = Counter(s.lower())
    return counter.get("p") == counter.get("y")


if __name__ == "__main__":
    i = "pPoooyY"
    print(solution(i))