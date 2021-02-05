from functools import lru_cache


class Solution:
    def letterCombinations(self, digits: str):
        button_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'], }

        @lru_cache(maxsize=None)
        def combination(data):
            if len(data) == 0:
                return []
            if len(data) == 1:
                return button_map[data]
            append = button_map[data[-1]]
            base = combination(data[:-1])
            result = []
            for comb in base:
                for app in append:
                    result.append(comb+app)
            return result

        return combination(digits)


s = Solution()
i = '23'
o = s.letterCombinations(i)
print(o)
