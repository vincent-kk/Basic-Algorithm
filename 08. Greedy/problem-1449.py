import sys

input = sys.stdin.readline

n, l = map(int, input().split())
location = list(map(int, input().split()))

location.sort()

need_to_fix = 1
coverange = location[0] + l - 1

for point in location:
    if point > coverange:
        need_to_fix += 1
        coverange = point + l - 1

print(need_to_fix)
