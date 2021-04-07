import re


remove = re.compile(r"\w+|\d+|[-]+|[_]+|[.]+")


def solution(new_id: str):
    id = new_id.lower()

    temp = remove.findall(id)
    id = "".join(temp)

    id = re.sub(r"[.]+", ".", id)
    id = re.sub(r"^[.]|[.]$", "", id)
    id = "a" if len(id) == 0 else id

    if len(id) > 15:
        id = id[:15]
        id = re.sub(r"[.]*$", "", id)
    if len(id) < 3:
        while len(id) < 3:
            id += id[-1]

    return id


if __name__ == "__main__":
    i = "=.="
    print(solution(i))