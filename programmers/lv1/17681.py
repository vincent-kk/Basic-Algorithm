from typing import List


def solution(n: int, arr1: List[int], arr2: List[int]):
    """[summary]
    프로도의 비밀지도 해독 프로그램
    지도는 공백과 벽으로 구성되어 있음
    전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있음
    두 지도에서 하나라도 벽인 부분은 벽이다 OR
    두 지도에서 둘 모두 공백인 부분은 공백이다 AND
    두 지도는 각 값을 이진수로 바꿨을때, 1이 벽이고 0이 공백이다
    Args:
        n (int): 지도의 가로와 세로 길이 (지도는 정사각형)
        arr1 (List[int]): 지도 1의 10진수 코드
        arr2 (List[int]): 지도 2의 10진수 코드

    Returns:
        List[int]: 완성된 지도
    """
    answer = []
    for i in range(n):
        row1 = format(arr1[i], "b")  # bin(arr1[i])[2:]
        row1 = list(map(int, row1.zfill(n)))
        row2 = format(arr2[i], "b")  # bin(arr2[i])[2:]
        row2 = list(map(int, row2.zfill(n)))
        row = []
        for b1, b2 in zip(row1, row2):
            row.append("#" if b1 or b2 else " ")
        answer.append("".join(row))
    return answer


if __name__ == "__main__":
    n = 5
    i1 = [9, 20, 28, 18, 11]
    i2 = [30, 1, 21, 17, 28]
    o = ["#####", "# # #", "### #", "#  ##", "#####"]
    print(solution(n, i1, i2) == o)
