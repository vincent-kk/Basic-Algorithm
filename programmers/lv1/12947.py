"""
[summary] x의 자릿수의 합으로 x가 나누어 떨어져야 한다.
[return] 그렇다면 true, 아니라면 false
"""


def solution(x: int):
    return not (x / sum(list(map(int, str(x))))) % 1


if __name__ == "__main__":
    i = 12
    print(solution(i))