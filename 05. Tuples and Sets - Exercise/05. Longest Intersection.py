n = int(input())
longest_intersection = []
longest_len = 0
a = set()
b = set()
for _ in range(n):
    data = input().split("-")
    data_a = data[0].split(",")
    data_b = data[1].split(",")
    a = set(range(int(data_a[0]), int(data_a[1]) + 1))
    b = set(range(int(data_b[0]), int(data_b[1]) + 1))
    c = a.intersection(b)
    if len(c) > longest_len:
        longest_len = len(c)
        longest_intersection = c
        longest_intersection = [int(x) for x in longest_intersection]
print(f"Longest intersection is {longest_intersection} with length {longest_len}")
