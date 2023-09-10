size = int(input())
matrix = []
for _ in range(size):
    matrix.append([int(el) if el.isdigit() else el for el in input().split()])

alice_cur_pos = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "A":
            alice_cur_pos = [row, col]
            matrix[row][col] = "*"

tea_bags_collected = 0
end_game = False
while tea_bags_collected < 10:
    cmd = input()
    if cmd == "up":
        if 0 > alice_cur_pos[0] - 1:
            end_game = True
            break
        else:
            alice_cur_pos[0] -= 1
            if matrix[alice_cur_pos[0]][alice_cur_pos[1]] == "R":
                matrix[alice_cur_pos[0]][alice_cur_pos[1]] = "*"
                end_game = True
                break
            else:
                if isinstance(matrix[alice_cur_pos[0]][alice_cur_pos[1]], int):
                    tea_bags_collected += matrix[alice_cur_pos[0]][alice_cur_pos[1]]
                matrix[alice_cur_pos[0]][alice_cur_pos[1]] = "*"
    elif cmd == "down":
        if alice_cur_pos[0] + 1 > size - 1:
            end_game = True
            break
        else:
            alice_cur_pos[0] += 1
            if matrix[alice_cur_pos[0]][alice_cur_pos[1]] == "R":
                matrix[alice_cur_pos[0]][alice_cur_pos[1]] = "*"
                end_game = True
                break
            else:
                if isinstance(matrix[alice_cur_pos[0]][alice_cur_pos[1]], int):
                    tea_bags_collected += matrix[alice_cur_pos[0]][alice_cur_pos[1]]
                matrix[alice_cur_pos[0]][alice_cur_pos[1]] = "*"
    elif cmd == "right":
        if alice_cur_pos[1] + 1 > size - 1:
            end_game = True
            break
        else:
            alice_cur_pos[1] += 1
            if matrix[alice_cur_pos[0]][alice_cur_pos[1]] == "R":
                matrix[alice_cur_pos[0]][alice_cur_pos[1]] = "*"
                end_game = True
                break
            else:
                if isinstance(matrix[alice_cur_pos[0]][alice_cur_pos[1]], int):
                    tea_bags_collected += matrix[alice_cur_pos[0]][alice_cur_pos[1]]
                matrix[alice_cur_pos[0]][alice_cur_pos[1]] = "*"
    elif cmd == "left":
        if 0 > alice_cur_pos[1] - 1:
            end_game = True
            break
        else:
            alice_cur_pos[1] -= 1
            if matrix[alice_cur_pos[0]][alice_cur_pos[1]] == "R":
                matrix[alice_cur_pos[0]][alice_cur_pos[1]] = "*"
                end_game = True
                break
            else:
                if isinstance(matrix[alice_cur_pos[0]][alice_cur_pos[1]], int):
                    tea_bags_collected += matrix[alice_cur_pos[0]][alice_cur_pos[1]]
                matrix[alice_cur_pos[0]][alice_cur_pos[1]] = "*"

if end_game:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
[print(*row) for row in matrix]
