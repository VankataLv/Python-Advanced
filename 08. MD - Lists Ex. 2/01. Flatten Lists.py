# matrix = [el for el in input().split("|") if el != " "]
# print(matrix)

line = input().split("|")
sub_lists = []
for sub_string in line[::-1]:
    sub_lists.extend(sub_string.split())
print(f"{' '.join(sub_lists)}")