from typing import List


def solution(brown: int, yellow: int) -> List[int]:
    """
    갈색의 격자 수, 노란색의 격자 수를 입력받아서, 전체 카펫의 크기를 계산

    Args:
        brown (int): 갈색의 격자 수 [8:5000]
        yellow (int): 노란색의 격자 수 [1:2000000]

        카펫의 가로는 세로와 같거나 세로보다 길다.

    Returns:
        List[int]: 카펫의 크기 [w,h]
    """
    area = brown + yellow
    b = (brown + 4) // 2
    dit = (b * b - 4 * area) ** (1 / 2)
    x = int((b + dit) // 2)
    return sorted([x, area // x], reverse=True)


if __name__ == "__main__":
    b, y = 10, 2
    print(solution(b, y))
