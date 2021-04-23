def solution(n, words):
    prev = ""
    used_words = set()
    for i, word in enumerate(words):
        if i == 0:
            used_words.add(word)
            prev = word
            continue
        if (word in used_words) or word[0] != prev[-1]:
            return [(i % n) + 1, (i // n) + 1]

        used_words.add(word)
        prev = word
    return [0, 0]
