from typing import List
from collections import Counter
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
    # data = sorted(s, key=lambda x: len(x))
    s = re.findall(r"\d+", s)
    count = Counter(s)
    data = [(int(k), count[k]) for k in count.keys()]
    data.sort(key=lambda x: x[1], reverse=True)
    return [x for x, c in data]


if __name__ == "__main__":
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))