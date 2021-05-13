from typing import List


def solution(n: int, t: int, m: int, timetable: List[str]) -> str:
    """
    셔틀 운행 시간
    9:00부터 n회 t분 간격으로 역에 도착, 한 버스에는 m명이 탑승 가능
    버스의 도착 시간과 동일한 시간에 도착한 사람까지 탈 수 있다
    모든 탑승자가 도착하는 시간 table이 주어질 때,
    가장 마지막으로 탑승할 수 있는 시간을 구하라

    Args:
        n (int): 버스의 운행 횟수
        t (int): 버스 운행 간격
        m (int): 버스 정원
        timetable (List[str]): 탑승자가 역에 도착하는 시간

    Returns:
        str: 마지막으로 탑승할 수 있는 버스의 시간
    """
    if n == 1:
        return "09:00"
    timetable = [
        int(time.split(":")[0]) * 60 + int(time.split(":")[1]) for time in timetable
    ]
    timetable.sort()
    start = 9 * 60
    end = start + t * (n - 1)

    for i in range(n):
        time = end - i * t
        # prev = end - (i + 1) * t + 1
        count = 0
        while timetable and time - t < timetable[-1]:
            count += 1
            timetable.pop()
    return


if __name__ == "__main__":
    n, t, m, table = 1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]
    print(solution(n, t, m, table))
