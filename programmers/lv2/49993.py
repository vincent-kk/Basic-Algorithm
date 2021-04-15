from typing import List


def solution(skill: str, skill_trees: List[str]) -> int:
    """[summary]
    가능한 스킬트리인지를 검증. 가능한 스킬트리의 개수를 반환
    Args:
        skill (str): 선행스킬
        skill_trees (List[str]): 제시된 스킬트리
      * 선행스킬이 모두 등장하지 않을 수 있다.
    Returns:
        int: 제시된 스킬트리 중 가능한 스킬트리의 수
    """
    answer = 0
    for skill_tree in skill_trees:
        skill_index = [skill_tree.find(s) for s in skill]

        if skill_index[0] < 0:
            if max(skill_index) >= 0:
                continue

        while len(skill_index) > 0:
            if skill_index[-1] < 0:
                skill_index.pop()
            else:
                break

        valid = True
        prev = -1
        for s in skill_index:
            if s < prev:
                valid = False
                break
            prev = s
        if valid:
            answer += 1

    return answer


if __name__ == "__main__":
    s = "CBD"
    tree = ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(s, tree))
