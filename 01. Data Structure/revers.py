import sys

input = sys.stdin.readline


def printAll(stack):
    while len(stack) > 0:
        print(stack.pop(), end='')


def reversStr(str):
    for ch in str:
        if ch == ' ':
            printAll(s)
            print(' ', end='')
        else:
            s.append(ch)
    printAll(s)
    print('')


s = []
t = int(input())

for _ in range(t):
    str = input()
    reversStr(str[:-1])
