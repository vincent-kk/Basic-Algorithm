# import sys

# input = sys.stdin.readline


# def solution(line: str):
#     tags = []
#     temp = []
#     isTag = False
#     for ch in line:
#         if ch == "<":
#             isTag = True
#             continue
#         if isTag:
#             if ch == ">":
#                 isTag = False
#                 tags.append("".join(temp))
#                 temp.clear()
#                 continue
#             temp.append(ch)

#     stack = []
#     for t in tags:
#         tag = t.split()
#         if len(stack) == 0:
#             if not (len(tag) > 1 and tag[1] == "/"):
#                 stack.append(tag[0])
#         else:
#             if tag[0][0] == "/":
#                 if stack[-1] == tag[0][1:]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 if not (len(tag) > 1 and tag[1] == "/"):
#                     stack.append(tag[0])

#     return len(stack) == 0


# if __name__ == "__main__":
#     while True:
#         line = input()[:-1]
#         if line == "#":
#             break
#         print("legal" if solution(line) else "illegal")


def check(data):
    s = []
    tag = False
    temp = ""
    for i in range(len(data)):
        if data[i] == "<":
            tag = True
        elif data[i] == ">":
            tag = False
            if temp and temp[-1] == "/":
                temp = ""
                continue
            elif s and s[-1] == temp[1:]:
                s.pop()
            else:
                s.append(temp)
            temp = ""

        if tag and data[i] == " " and data[i + 1] != "/":
            tag = False

        if tag and data[i] != "<":
            temp += data[i]

    if s:
        print("illegal")
    else:
        print("legal")


while True:
    data = input()
    if data == "#":
        break
    else:
        check(data)