from typing import List
from string import ascii_uppercase


def solution(msg: str) -> List[int]:
    answer = []
    words = dict((w, i + 1) for i, w in enumerate(ascii_uppercase))

    index = 27
    prev = ""
    for m in msg:
        if prev + m in words:
            prev += m
        else:
            answer.append(words[prev])
            words[prev + m] = index
            index += 1
            prev = m
    else:
        answer.append(words[prev])

    return answer


if __name__ == "__main__":
    i = "TOBEORNOTTOBEORTOBEORNOT"
    print(solution(i))
