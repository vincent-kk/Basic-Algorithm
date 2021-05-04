import collections


class Solution:
    def minSteps(self, s: str, t: str):
        cache = collections.defaultdict(int)
        for c in s:
            cache[c] += 1

        for c in t:
            if cache[c]:
                cache[c] -= 1

        return sum(cache.values())


if __name__ == "__main__":
    S = Solution()
    s = "leetcode"
    t = "practice"
    o = S.minSteps(s, t)
    print(o)


# import collections


# s = "leetcode"
# t = "practice"
# memo = collections.defaultdict(int)
# for char in s:
#     memo[char] += 1
# for char in t:
#     if memo[char]:
#         memo[char] -= 1
# print(sum(memo.values()))
