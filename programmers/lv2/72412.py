from typing import List
from itertools import combinations
from bisect import bisect_left


def solution(info: List[str], queries: List[str]) -> List[int]:
    """
    지원자의 정보를 토대로 입력된 쿼리에 부합하는 지원자의 수를 리턴

    Args:
        info (List[str]): 각각의 지원자의 정보를 " "로 구분하여 저장 [1:50000]
        query (List[str]): 각각의 쿼리를 " "로 구분하여 저장 [1:100000]
        "cpp and - and senior and pizza 500"
        "cpp로 코딩테스트를 봤으며, 경력은 senior 이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 500점 이상 받은 사람"

    Returns:
        List[int]: 각 쿼리별로 만족하는 사람의 수 [1:100000]
    """
    # 단순 반복

    # info = [tuple(person.split()) for person in info]
    # answer = []
    # for raw in queries:
    #     query = raw.split(" ")
    #     query = list(filter(lambda q: q != "and", query))
    #     scop = info[:]
    #     for i, q in enumerate(query[:-1]):
    #         if q == "-":
    #             continue
    #         scop = list(filter(lambda p: p[i] == q, scop))
    #     scop = list(filter(lambda p: int(p[-1]) >= int(query[-1]), scop))
    #     answer.append(len(scop))
    # return answer

    # set과 id를 사용한 속도 개선. 효율성 통과 x
    # info = [(id, tuple(person.split())) for id, person in enumerate(info)]
    # # universe = set(range(len(info)))
    # data_map = [
    #     {
    #         "python": set(
    #             [id for id, data in filter(lambda p: p[1][0] == "python", info)]
    #         ),
    #         "java": set([id for id, data in filter(lambda p: p[1][0] == "java", info)]),
    #         "cpp": set([id for id, data in filter(lambda p: p[1][0] == "cpp", info)]),
    #     },
    #     {
    #         "backend": set(
    #             [id for id, data in filter(lambda p: p[1][1] == "backend", info)]
    #         ),
    #         "frontend": set(
    #             [id for id, data in filter(lambda p: p[1][1] == "frontend", info)]
    #         ),
    #     },
    #     {
    #         "senior": set(
    #             [id for id, data in filter(lambda p: p[1][2] == "senior", info)]
    #         ),
    #         "junior": set(
    #             [id for id, data in filter(lambda p: p[1][2] == "junior", info)]
    #         ),
    #     },
    #     {
    #         "chicken": set(
    #             [id for id, data in filter(lambda p: p[1][3] == "chicken", info)]
    #         ),
    #         "pizza": set(
    #             [id for id, data in filter(lambda p: p[1][3] == "pizza", info)]
    #         ),
    #     },
    #     dict([(id, int(data[4])) for id, data in info]),
    # ]
    # answer = []
    # for raw in queries:
    #     query = raw.split(" ")
    #     query = list(filter(lambda q: q != "and", query))
    #     group = set(range(len(info)))
    #     for i, q in enumerate(query[:-1]):
    #         if q == "-":
    #             continue
    #         group &= data_map[i][q]

    #     group = set(filter(lambda p: data_map[4][p] >= int(query[-1]), group))
    #     answer.append(len(group))

    # return answer

    # 실패 후 답 검색... 이건 내가 생각해내서 풀 수는 없는 문제였던 듯...

    data_map = dict()
    for d in info:
        infomation = d.split()
        keys = infomation[:-1]
        data = int(infomation[-1])
        for n in range(5):
            key_comb = list(combinations(keys, n))
            for k in key_comb:
                key = "".join(k)
                if key in data_map:
                    data_map[key].append(data)
                else:
                    data_map[key] = [data]
    for key in data_map.keys():
        data_map[key].sort()

    answer = []
    for raw in queries:
        query = raw.replace("and", "").replace("-", "").split()
        q_keys = query[:-1]
        q_value = int(query[-1])

        q_key = "".join(q_keys)
        if not q_key in data_map:
            answer.append(0)
        else:
            values = data_map[q_key]
            answer.append(len(values) - bisect_left(values, q_value))

    return answer


if __name__ == "__main__":
    i = [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50",
    ]
    q = [
        "- and - and - and - 150",
    ]
    print(solution(i, q))
