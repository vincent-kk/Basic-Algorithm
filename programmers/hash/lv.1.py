from collections import defaultdict


def solution(participant, completion):
    note = defaultdict(int)
    for person in participant:
        note[person] += 1

    for person in completion:
        if person in note:
            note[person] -= 1
            if note[person] == 0:
                del note[person]
    return note.popitem()[0]


if __name__ == "__main__":
    i = ["leo", "kiki", "eden"]
    c = ["eden", "kiki"]
    print(solution(i, c))
