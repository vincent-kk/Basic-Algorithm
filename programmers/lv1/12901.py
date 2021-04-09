def solution(a, b):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num = 4
    for m in range(a - 1):
        num += month[m]
    num += b
    return days[num % 7]


if __name__ == "__main__":
    i = 5
    c = 24
    print(solution(i, c))
