def operate(operator, *args):
    def add():
        res = sum(args)
        return res

    def subtract():
        res = 0
        for cur_num in args:
            res -= abs(cur_num)
        return res

    def multiply():
        res = 1
        for cur_num in args:
            res *= cur_num
        return res

    def divide():
        res = 1
        for cur_num in args:
            res /= cur_num
        return res

    if operator == "+":
        return add()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return divide()

print(operate("-", 1, 2, 3))

