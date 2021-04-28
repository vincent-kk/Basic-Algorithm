from typing import List
import re


def solution(files: List[str]) -> List[str]:
    data = dict()
    for file in files:
        head, num, *tail = re.split(r"(\d{1,5})", file)
        data[file] = (head.lower(), int(num))

    files.sort(key=lambda f: data[f][1])
    files.sort(key=lambda f: data[f][0])

    return files


if __name__ == "__main__":
    i = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    print(solution(i))
