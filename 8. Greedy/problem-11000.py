import sys
from operator import itemgetter

input = sys.stdin.readline

num = int(input())
classes = []

for _ in range(num):
    start, end = map(int, input().split())
    classes.append((start, end))
classes.sort(key=itemgetter(0))

num_of_classroom = 0
closest_end = []
while len(classes) > 0:
    start, end = classes.pop(0)
    if len(closest_end) == 0 or closest_end[0] > start:
        num_of_classroom += 1
    else:
        closest_end.pop()

    closest_end.append(end)
    closest_end.sort()

    # index = 0
    # while index < len(classes):
    #     if end <= classes[index][0]:
    #         start, end = classes.pop(index)
    #         index -= 1
    #     index += 1

print(num_of_classroom)