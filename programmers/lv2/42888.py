from typing import List


def solution(records: List[str]):

    logger = []
    id_name = dict()
    for record in records:
        op, id, *name = record.split()
        if name:
            id_name[id] = name[0]
        if op == "Enter":
            msg = "님이 들어왔습니다."
        if op == "Leave":
            msg = "님이 나갔습니다."
        if op == "Change":
            continue
        logger.append((id, msg))
    answer = []
    for log in logger:
        id, msg = log
        answer.append(id_name[id] + msg)
    return answer


if __name__ == "__main__":
    i = [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan",
    ]

    print(solution(i))