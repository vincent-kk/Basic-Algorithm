def solution(n, arr1, arr2):
    answer = []
    l = 4
    m = max(arr1 + arr2)
    l = len(format(m, "b"))

    for e1, e2 in zip(arr1, arr2):
        e1_b = format(e1, "b").rjust(l, "0")
        e2_b = format(e2, "b").rjust(l, "0")
        row = ""
        for b1, b2 in zip(e1_b, e2_b):
            if b1 == "1" or b2 == "1":
                row += "#"
            else:
                row += " "
        answer.append(row)
    return answer