# class Stack:
#     stack = []

#     def push(self, e):
#         self.stack.append(e)

#     def pop(self):
#         if self.empty() == 1:
#             return -1
#         else:
#             return self.stack.pop()

#     def top(self):
#         if self.empty() == 1:
#             return -1
#         else:
#             return self.stack[-1]

#     def size(self):
#         return len(self.stack)

#     def empty(self):
#         if self.size() == 0:
#             return 1
#         else:
#             return 0

# s = Stack()

import sys

input = sys.stdin.readline

s = []
n = int(input())

for _ in range(n):
    raw = input()[:-1]
    if raw == "pop":
        print(s.pop() if (len(s) > 0) else -1)
    elif raw == "top":
        print(s[-1] if (len(s) > 0) else -1)
    elif raw == "size":
        print(len(s))
    elif raw == "empty":
        print(0 if len(s) > 0 else 1)
    else:
        op, arg = raw.split()
        s.append(int(arg))
