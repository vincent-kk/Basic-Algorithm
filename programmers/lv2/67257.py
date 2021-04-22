import re

from itertools import permutations


def solution(expression):
    priorities = list(permutations(["*", "+", "-"]))
    expression = re.split(r"([+]|[-]|[*])", expression)

    def calc(exp, priority):
        _exp = exp[:]
        for op in priority:
            while op in _exp:
                i = _exp.index(op)
                x, y = int(_exp[i - 1]), int(_exp[i + 1])
                if op == "*":
                    _exp[i - 1] = str(x * y)
                if op == "-":
                    _exp[i - 1] = str(x - y)
                if op == "+":
                    _exp[i - 1] = str(x + y)
                _exp = _exp[:i] + _exp[i + 2 :]
        return int(_exp[0])

    answer = -1
    for p in priorities:
        answer = max(answer, abs(calc(expression, p)))
    return answer


# def solution(expression):
#     priorities = ["*-+", "*+-", "-*+", "-+*", "+-*", "+*-"]
#     expression = re.split(r"([+]|[-]|[*])", expression)

#     def calc(exp, p):

#         operator = []
#         operand = []

#         for e in exp:
#             if e.isdigit():
#                 operand.append(int(e))
#             else:
#                 if not operator:
#                     operator.append(e)
#                     continue
#                 while operator and (p.find(operator[-1]) > p.find(e)):
#                     y = operand.pop()
#                     x = operand.pop()
#                     op = operator.pop()
#                     if op == "*":
#                         operand.append(x * y)
#                     elif op == "+":
#                         operand.append(x + y)
#                     elif op == "-":
#                         operand.append(x - y)
#                 operator.append(e)

#         while operand and operator:
#             y = operand.pop()
#             x = operand.pop()
#             op = operator.pop()
#             if op == "*":
#                 operand.append(x * y)
#             elif op == "+":
#                 operand.append(x + y)
#             elif op == "-":
#                 operand.append(x - y)

#         return operand[0]

#     answer = -1
#     for p in priorities:
#         answer = max(answer, abs(calc(expression, p)))
#     return answer


if __name__ == "__main__":
    i = "100-200*300-500+20"
    print(solution(i))
