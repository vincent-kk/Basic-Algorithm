import sys

input = sys.stdin.readline

while True:
    L, R, C = map(int, input().split())
    if L == R == C:
        break
    building = []
    start = (0, 0, 0)
    end = (0, 0, 0)
    for f in range(L):
        floor = []
        for r in range(R):
            line = list(input()[:-1])
            if "S" in line:
                start = (f, r, line.find("S"))
            if "D" in line:
                end = (f, r, line.find("D"))
            line = list(map(lambda e: 0 if e == "#" else 1))
            floor.append(line)
