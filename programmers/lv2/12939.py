def solution(s):
    l = list(map(int, s.split()))
    return f"{min(l)} {max(l)}"