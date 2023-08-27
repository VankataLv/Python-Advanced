std_count = int(input())
std_db = {}
for _ in range(std_count):
    name, grade = tuple(input().split())
    grade = float(grade)
    if name not in std_db:
        std_db[name] = []
    std_db[name].append(grade)

for key, value in std_db.items():
    cur_std_avg = sum(value) / len(value)
    print(f"{key} -> {' '.join([str(f'{el:.2f}') for el in value])} (avg: {cur_std_avg:.2f})")


# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00

# 4
# Scott 4.50
# Ted 3.00
# Scott 5.00
# Ted 3.66

# 5
# Lee 6.00
# Lee 5.50
# Lee 6.00
# Peter 4.40
# Kenny 3.30