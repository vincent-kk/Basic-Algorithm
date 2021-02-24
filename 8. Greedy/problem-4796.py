import sys

input = sys.stdin.readline

index = 0
while True:

    unit_usable, unit_period, vacation = map(int, input().split())

    if unit_usable == 0 or unit_period == 0 or vacation == 0:
        break

    index += 1
    can_use = 0

    while unit_period < vacation:
        can_use += unit_usable
        vacation -= unit_period

    can_use += vacation if (vacation < unit_usable) else unit_usable
    print(f"Case {index}: {can_use}")
