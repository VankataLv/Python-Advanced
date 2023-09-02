from collections import deque
from math import floor

expression = deque(input())
left_side = deque()
operators = ["*", "+", "-", "/"]
new = ""


def calculate(operator: str, exp):
    new_exp = ""
    if operator == "+":
        new_exp = exp.popleft()
        for _ in range(len(exp)):
            new_exp += exp.popleft()
    elif operator == "-":
        new_exp = exp.popleft()
        for _ in range(len(exp)):
            new_exp -= exp.popleft()
    elif operator == "*":
        new_exp = 1
        for _ in range(len(exp)):
            new_exp *= exp.popleft()
    elif operator == "/":
        new_exp = exp.popleft()
        for _ in range(len(exp)):
            new_exp /= exp.popleft()
            new_exp = floor(new_exp)

    return new_exp


while len(expression) > 1:
    cur_char = expression.popleft()
    if cur_char == " ":
        continue
    elif cur_char in operators:
        if cur_char == "-":
            if expression[0].isnumeric():
                while expression[0] != " ":
                    cur_char += expression.popleft()
                cur_char = int(cur_char)
                left_side.append(cur_char)

            else:
                expression.appendleft(calculate("-", left_side))
        else:
            expression.appendleft(calculate(cur_char, left_side))
    else:
        while expression[0] != " ":
            cur_char += expression.popleft()
        cur_char = int(cur_char)
        left_side.append(cur_char)

print(calculate(expression.popleft(), left_side))
