rows, columns = [int(el) for el in input().split()]
matrix = [[el for el in input().split()] for _ in range(rows)]
cmd = input()
while cmd != "END":
    keyword, *data = cmd.split()
    if keyword == "swap":
        if len(data) == 4:
            data = [int(el) for el in data]
            if data[0] in range(rows) and data[2] in range(rows):
                if data[1] in range(columns) and data[3] in range(columns):
                    row_1, col_1, row_2, col_2 = [int(el) for el in data]
                    matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
                    [print(*row) for row in matrix]
                else:
                    print("Invalid input!")
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    cmd = input()

# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END
