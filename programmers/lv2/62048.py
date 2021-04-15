from math import gcd


def solution(w: int, h: int):

    # 계산수를 줄인 구분구적법 사용 O(w/gcd)
    # g = gcd(w, h)
    # dw = w // g
    # dh = h // g
    # dx = dh / dw
    # s = dw * dh
    # for x in range(1, dw):
    #     s -= int(dx * x) * 2

    # return w * h - s * g

    # 구분구적법을 사용한 방법 O(w)
    answer = 0
    for i in range(1, w):
        answer += i * h // w
    return answer * 2

    # 씨발년들
    # return w * h - (w + h - gcd(w, h))


if __name__ == "__main__":
    w = 8
    h = 12
    print(solution(w, h))
