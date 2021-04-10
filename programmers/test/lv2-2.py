from typing import List


def solution(skill: str, skill_trees: List[str]):
    answer = len(skill_trees)
    for sk in skill_trees:
        prev = -1
        okay = True
        for s in skill:
            i = sk.find(s)
            if i < 0:
                if okay:
                    okay = False
                continue
            if prev > i:
                answer -= 1
                break
            else:
                if not okay:
                    answer -= 1
                    break
                prev = i

    return answer


if __name__ == "__main__":
    i = "CBD"
    it = ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(i, it))
