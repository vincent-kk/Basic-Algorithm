# from collections import defaultdict


# def solution(n):
#     dp = defaultdict(int)
#     dp[1] = 1
#     for i in range(2,n+1):
#     local_min = -1
#     for j in range(i//2,i):
#         if local_min < 0:
#             local_min = dp[i-j]+j
#         else:
#             local_min = (dp[i-j]+j if dp[i-j]+j < local_min else local_min)
#     if i % 2:
#         local_min = local_min = (dp[(i-1)//2]+1 if dp[(i-1)//2]+1 < local_min else local_min)
#     else:
#         local_min =local_min = (dp[(i)//2] if dp[(i)//2] < local_min else local_min)
#     dp[i] = (dp[(i-1)//2]+1 if i%2 else dp[(i)//2])

#     def do(n):
#         if n == 1:
#             return 1
#         if n % 2:
#             return do((n - 1) // 2) + 1
#         else:
#             return do(n // 2)

#     return do(n)


def solution(n):
    answer = 1
    while n > 1:
        if n % 2:
            n -= 1
            answer += 1
        n = n // 2

    return answer