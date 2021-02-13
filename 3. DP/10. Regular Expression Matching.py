class Solution:
    def isMatch(self, s: str, p: str):
        def match(target, char):
            return target == char or char == "."

        pattern = list(p)

        index = 0
        while index < len(s) and len(pattern) > 0:
            char = pattern.pop(0)
            if len(pattern) > 0 and pattern[0] == "*":
                pattern.pop(0)
                stop = "."
                if len(pattern) > 0 and char == ".":
                    stop = pattern[0]
                while index < len(s) and match(s[index], char):
                    if s[index] == stop:
                        break
                    index += 1

            else:
                if not match(s[index], char):
                    return False
                index += 1

        return index == len(s) and len(pattern) == 0


s = Solution()
i1 = "aaa"
i2 = "a*a"

print(s.isMatch(i1, i2))
