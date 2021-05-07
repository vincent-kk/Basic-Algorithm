class Solution(object):
    def numberOfMatches(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        answer = 0
        while n > 1:
            if n % 2:
                n = (n - 1) // 2
                answer += n
                n += 1
            else:
                n = n // 2
                answer += n
        return answer


if __name__ == "__main__":
    S = Solution()
    print(S.numberOfMatches(7))