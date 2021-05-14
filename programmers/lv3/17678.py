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

    # 모든 정보를 분으로 변환
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()

    # 모든 버스의 시간을 배열로 생성
    bustime = [9 * 60 + t * i for i in range(n)]

    answer = 0

    # 현재까지 탑승한 크루의 인덱스 번호
    crew = 0
    for bus in bustime:
        # 이번에 버스에 탄 크루의 수
        count = 0
        # count < m  : 버스에 자리가 있다
        # crew < len(timetable) : 크루 인덱스가 크루 배열 내에 있다
        # timetable[crew] <= bus : 크루가 도착한 시간이 버스 시간보다 같거나 작다
        while count < m and crew < len(timetable) and timetable[crew] <= bus:
            # 그 크루를 태우고, 크루 인덱스를 증가시킨다
            crew += 1
            count += 1

        # 이번 버스에서 버스가 가득 차지 않았다면, 버스 도착 시간과 동일한 시간에 도착하면 된다
        if count < m:
            answer = bus
        # 버스가 가득 찼다면 그 버스에 마지막으로 탄 사람보다 1분 빨리 오면 된다
        else:
            # 크루 인덱스의 마지막이므로, 이전 시간에 타지 못한 크루의 수를 고려할 수 있다
            answer = timetable[crew - 1] - 1

    # 모든 버스 시간표에 대해서 위 계산을 수행한 후 마지막에 업데이트 된 시간이 가장 늦게 탈 수 있는 시간이다
    return "{:02d}:{:02d}".format(answer // 60, answer % 60)


if __name__ == "__main__":
    n, t, m, table = 2, 10, 2, ["09:10", "09:09", "08:00"]
    print(solution(n, t, m, table))
