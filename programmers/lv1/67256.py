from typing import List

buttons = {
    1: (0, 0),
    2: (1, 0),
    3: (2, 0),
    4: (0, 1),
    5: (1, 1),
    6: (2, 1),
    7: (0, 2),
    8: (1, 2),
    9: (2, 2),
    0: (1, 3),
    "*": (0, 3),
    "#": (2, 3),
}


def solution(numbers: List[int], hand: str):
    left = {1, 4, 7}
    right = {3, 6, 9}
    lPos = (0, 3)
    rPos = (2, 3)
    isRight = hand == "right"
    answer = []
    for n in numbers:
        if n in left:
            answer.append("L")
            lPos = buttons[n]
        elif n in right:
            answer.append("R")
            rPos = buttons[n]
        else:
            pos = buttons[n]
            lLen = abs(lPos[0] - pos[0]) + abs(lPos[1] - pos[1])
            rLen = abs(rPos[0] - pos[0]) + abs(rPos[1] - pos[1])
            if lLen == rLen:
                if isRight:
                    answer.append("R")
                    rPos = pos
                else:
                    answer.append("L")
                    lPos = pos
            else:
                if lLen > rLen:
                    answer.append("R")
                    rPos = pos
                else:
                    answer.append("L")
                    lPos = pos

    return "".join(answer)


if __name__ == "__main__":
    i = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    h = "right"
    print(solution(i, h))
