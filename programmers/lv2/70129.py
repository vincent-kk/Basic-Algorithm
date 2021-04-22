from collections import Counter


def solution(s):
    convert_binery = 0
    removed_zero = 0
    while s != "1":
        counter = Counter(s)
        removed_zero += counter["0"]
        s = format(counter["1"], "b")
        convert_binery += 1
    return convert_binery, removed_zero


if __name__ == "__main__":
    i = "110010101001"
    print(solution(i))