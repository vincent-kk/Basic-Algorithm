import sys

input = sys.stdin.readline

stack = []
pick = 1
result = ''

t = int(input()[:-1])

for i in range(t):
    n = int(input()[:-1])

    if len(stack) == 0 or stack[-1] < n:
        for _ in range(pick, n + 1):
            stack.append(_)
            pick += 1
            result += '+'
        stack.pop()
        result += '-'
    elif stack[-1] == n:
        stack.pop()
        result += '-'
    else:
        result = 'NO'
        break

if result == 'NO':
    print(result)
else:
    for op in result:
        print(op)