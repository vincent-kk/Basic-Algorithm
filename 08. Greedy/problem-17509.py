import sys

input = sys.stdin.readline

problems = []
for i in range(11):
    d, v = map(int, input().split())
    problems.append((d, v))

problems.sort()

penalty = 0
total_time = 0

for p in problems:
    total_time += p[0]
    penalty += total_time + 20 * p[1]

print(penalty)