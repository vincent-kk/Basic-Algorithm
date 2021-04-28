from typing import List
import heapq


def solution(lines: List[str]) -> int:

    traffic_log = []
    for line in lines:
        date, time, delay = line.split()
        time = time.split(":")
        time = (
            3600000 * int(time[0]) + 60000 * int(time[1]) + int(float(time[2]) * 1000)
        )

        delay = int(float(delay[:-1]) * 1000)
        traffic_log.append((time - delay + 1, time))
    traffic_log.sort()

    max_traffic = 1
    queue = []
    for start, end in traffic_log:

        while queue and queue[0] <= start - 1000:
            heapq.heappop(queue)

        heapq.heappush(queue, end)
        max_traffic = len(queue) if len(queue) > max_traffic else max_traffic

    return max_traffic


if __name__ == "__main__":
    i = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
    print(solution(i))