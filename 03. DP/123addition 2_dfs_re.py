from sys import stdin


def dfs(sum):
    global n, k, preorder, stack
    if sum > n:
        return
    if sum == n:
        preorder += 1

        if preorder == k:
            print(''.join(stack)[:-1])
            exit(0)

    for i in range(1, 4):
        stack.append('{}+'.format(i))
        dfs(sum+i)
        stack.pop()


preorder = 0
stack = []
n, k = map(int, stdin.readline().split())
dfs(0)
print(-1)
