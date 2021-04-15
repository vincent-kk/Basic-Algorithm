import re


def solution(dartResult: str) -> int:
    """[summary]
    다트 점수 계산 프로그램 총 3회
    Args:
        dartResult (str): 점수|보너스|옵션 구성의 문자열
        S, D ,T : 점수**1 , 점수**2, 점수**3, 점수마다 1개씩 존재
        * : 이번 획득 점수와 이전 획득 점수를 2배로, 처음에 나올 경우 현재점수 2배만
        # : -이번 획득 점수
        *+# : -이번 획득 점수*2
        *,# : 점수마다 둘 중 하나가 존재할 수도 있고 없을 수도 있음
    Returns:
        int: [description]
    """
    answer = 0

    scores = list(map(int, re.findall(r"\d+", dartResult)))
    bonus = list(filter(lambda x: x != "", re.split(r"\d+", dartResult)))

    length = len(scores)
    option = 1
    for i in range(length - 1, -1, -1):
        power = 1
        op = 1
        if bonus[i][0] == "D":
            power = 2
        if bonus[i][0] == "T":
            power = 3
        if len(bonus[i]) == 2:
            if bonus[i][1] == "*":
                op = 2
            if bonus[i][1] == "#":
                op = -1
        answer += option * op * scores[i] ** power
        option = 1
        if len(bonus[i]) == 2:
            if bonus[i][1] == "*":
                option = 2

    return answer


if __name__ == "__main__":
    i = "1T2D3D#"
    print(solution(i))