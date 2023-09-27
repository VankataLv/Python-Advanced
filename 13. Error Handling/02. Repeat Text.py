txt = input()
try:
    times = int(input())
    print(txt * times)
except ValueError:
    print("Variable times must be an integer")

