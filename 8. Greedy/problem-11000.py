import sys

# import heapq
from queue import PriorityQueue
from operator import itemgetter

input = sys.stdin.readline

N = int(input())

timeTable = [list(map(int, input().split())) for _ in range(N)]
timeTable.sort(key=itemgetter(0))

classrooms = PriorityQueue()
classrooms.put(timeTable[0][1])
# heapq.heappush(classrooms, timeTable[0][1])

for start, end in timeTable[1:]:
    if classrooms.queue[0] > start:
        classrooms.put(end)
        # heapq.heappush(classrooms, end)
    else:
        classrooms.get()
        classrooms.put(end)
        # heapq.heappop(classrooms)
        # heapq.heappush(classrooms, end)

print(len(classrooms.queue))

# classes = []

# for _ in range(num):
#     start, end = map(int, input().split())
#     classes.append((start, end))
# classes.sort(key=itemgetter(0))

# num_of_classroom = 0
# closest_end = []
# while len(classes) > 0:
#     start, end = classes.pop(0)
#     if len(closest_end) == 0 or closest_end[0] > start:
#         num_of_classroom += 1
#     else:
#         closest_end.pop()

#     closest_end.append(end)
#     closest_end.sort()

# index = 0
# while index < len(classes):
#     if end <= classes[index][0]:
#         start, end = classes.pop(index)
#         index -= 1
#     index += 1

# print(num_of_classroom)