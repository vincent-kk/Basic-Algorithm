from math import gcd


def solution(w: int, h: int):
    # g = gcd(w, h)
    # dw = w // g
    # dh = h // g
    # dx = dh / dw
    # s = dw * dh
    # for x in range(1, dw):
    #     s -= int(dx * x) * 2

    # return w * h - s * g

    # answer = 0
    # for i in range(1, w):
    #     answer += int(i * h / w)
    # return answer * 2

    return w * h - (w + h - gcd(w, h))


if __name__ == "__main__":
    w = 8
    h = 12
    print(solution(w, h))
