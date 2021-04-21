from typing import List


def solution(arr: List[List[int]]) -> List[int]:
    """
    0과 1로 이루어진 가로세로 2**n인 2차원 정사각 행렬이 있다.
    이것을 쿼드트리 방식으로 압축하고자 함
    1. 암축하고자 하는 영역을 s라 하자
    2. s 내부가 모두 같은 값이라면 s를 해당 숫자 하나로 압축한다
    3. 그렇지 않으면 s를 4등분하여 나눠진 정사각형에 대해 2.를 반복한다

    Args:
        arr (List[List[int]]): 입력배열

    Returns:
        List[int]: 압축 결과에서 0의 개수, 1의 개수
    """
    l = len(arr)

    def do(r, c, n, data) -> int:
        """
        DC방식으로 정사각형 분할

        Args:
            start (tuple): (0,0) 시작 원소 포함
            end (tuple): (l-1, l-1) 마지막 원소 포함

        Returns:
            int: 현재 영역에서 0, 1의 개수
        """
        if n == 1:
            return (0, 1) if data[r][c] else (1, 0)
        else:
            next_n = n // 2
            q = [
                do(r, c, next_n, data),
                do(r, c + next_n, next_n, data),
                do(r + next_n, c, next_n, data),
                do(r + next_n, c + next_n, next_n, data),
            ]
            # 때로는 무식하게 그냥 돌리는게 나을 수도 있다
            check = q[0] == q[1] == q[2] == q[3]
            if check and (q[0] == (0, 1) or q[0] == (1, 0)):
                return q[0]
            else:
                # zip문법을 기억해둬야겠다
                return tuple(map(sum, zip(*q)))

    return do(0, 0, l, arr)


if __name__ == "__main__":
    # arr = [[1, 1], [1, 0]]
    arr = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
    print(solution(arr))