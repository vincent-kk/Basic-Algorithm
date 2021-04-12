import re


def solution(s: str):
    regex = re.compile(r"^\d{4}$|^\d{6}$")
    return True if regex.match(s) else False
    # return s.isdigit() and len(s) in (4, 6)


if __name__ == "__main__":
    i = "2235a"
    print(solution(i))
