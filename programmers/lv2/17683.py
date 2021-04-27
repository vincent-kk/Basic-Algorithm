from typing import List


def solution(m: str, musicinfos: List[str]) -> str:
    target = []
    for ch in m:
        if ch == "#":
            target[-1] = target[-1].lower()
        else:
            target.append(ch)
    target = "".join(target)

    answer = "(None)"
    time = 0
    for music in musicinfos:
        start, end, name, mel = music.split(",")
        s_hh, s_mm = map(int, start.split(":"))
        e_hh, e_mm = map(int, end.split(":"))
        dt = 60 * (e_hh - s_hh) + (e_mm - s_mm)

        melody = []
        for ch in mel:
            if ch == "#":
                melody[-1] = melody[-1].lower()
            else:
                melody.append(ch)
        melody = "".join(melody)

        ml = len(melody)
        melody = melody * (dt // ml) + melody[: (dt % ml)]

        if target in melody:
            if dt > time:
                answer = name
                time = dt

    return answer


if __name__ == "__main__":
    m = "ABC"
    mu = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    print(solution(m, mu))
