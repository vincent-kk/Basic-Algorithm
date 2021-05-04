from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str):
        index_pattern = [pattern.index(ch) for ch in pattern]
        count_pattern = [pattern.count(ch) for ch in pattern]

        result = []

        for word in words:
            index_word = [word.index(x) for x in word]
            count_word = [word.count(x) for x in word]
            if index_word == index_pattern and count_word == count_pattern:
                result.append(word)

        return result