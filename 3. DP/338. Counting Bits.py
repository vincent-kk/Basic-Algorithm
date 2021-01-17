
def isPowerOfTwo(n):
    return n == (n & -n)


class Solution:
    def countBits(self, num: int):
        answer = [0]*(num+1)
        answer[0] = 0
        if num == 0:
            return answer
        answer[1] = 1
        if num == 1:
            return answer
        prevPowerOfTwo = 1
        for n in range(2, num+1):
            if isPowerOfTwo(n):
                prevPowerOfTwo = n
                answer[n] = 1
            else:
                answer[n] = 1 + answer[n-prevPowerOfTwo]
        return answer


s = Solution()
i = 5
a = s.countBits(i)
for o in a:
    print(o, end=', ')
