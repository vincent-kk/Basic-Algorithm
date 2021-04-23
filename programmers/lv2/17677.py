from collections import Counter


def solution(str1, str2):
    p1 = []
    p2 = []
    prev = ""
    for ch in str1:
        ch = ch.upper()
        if not ch.isalpha():
            prev = ""
            continue
        if not prev:
            prev = ch
            continue
        p1.append(prev + ch)
        prev = ch

    prev = ""
    for ch in str2:
        ch = ch.upper()
        if not ch.isalpha():
            prev = ""
            continue
        if not prev:
            prev = ch
            continue
        p2.append(prev + ch)
        prev = ch

    if not p1 and not p2:
        return 65536
    if not p1:
        return 0

    c1 = Counter(p1)
    c2 = Counter(p2)

    s1 = set(p1)
    s2 = set(p2)

    upper_set = s1 & s2
    buttom_set = s1 | s2

    u = sum([min(c1[s], c2[s]) for s in upper_set])
    b = sum([max(c1[s], c2[s]) for s in buttom_set])

    return int((u / b) * 65536)
