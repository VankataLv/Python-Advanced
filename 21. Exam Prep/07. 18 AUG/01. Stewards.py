from collections import deque

seats = [el for el in input().split(", ")]
first_seq = deque([int(el) for el in input().split(", ")])
second_seq = deque([int(el) for el in input().split(", ")])

rotations = 0
matched_seats = []
while True:
    if rotations == 10 or len(matched_seats) == 3:
        break
    cur_first_num = first_seq.popleft()
    cur_second_num = second_seq.pop()
    summed_nums = cur_first_num + cur_second_num
    char_found = chr(summed_nums)
    str_to_match_1 = str(cur_first_num) + char_found
    str_to_match_2 = str(cur_second_num) + char_found

    if str_to_match_1 in seats:
        if str_to_match_1 in matched_seats:
            pass
        else:
            matched_seats.append(str_to_match_1)
    elif str_to_match_2 in seats:
        if str_to_match_2 in matched_seats:
            pass
        else:
            matched_seats.append(str_to_match_2)
    else:
        first_seq.append(cur_first_num)
        second_seq.appendleft(cur_second_num)
    rotations += 1

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")
