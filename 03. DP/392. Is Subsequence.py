class Solution:
    def isSubsequence(self, s: str, t: str):
        sl, tl = len(s), len(t)
        sp, tp = 0, 0

        while sp < sl and tp < tl:
            if s[sp] == t[tp]:
                sp += 1
            tp += 1

        return sp == sl


if __name__ == "__main__":
    S = Solution()
    s = "abc"
    t = "ahbgdc"
    print(S.isSubsequence(s, t))
