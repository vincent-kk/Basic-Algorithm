from typing import List
import re


def solution(s: str) -> List[int]:
    """[summary]
    튜플: 순서가 있는 숫자의 열거형.
    * 중복이 없는 튜플 제공

    Args:
        s (str): 특정 튜플을 포함하는 열거형

    Returns:
        List[int]: 표현된 튜플
    """
    answer = []
    s = s[2:-2]
    l = sorted(s.split("},{"), key=lambda x: len(x))
    for element in l:
        for e in map(int, element.split(",")):
            if e not in answer:
                answer.append(e)
    return list(answer)


if __name__ == "__main__":
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))