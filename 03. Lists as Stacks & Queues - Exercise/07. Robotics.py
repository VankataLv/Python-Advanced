from collections import deque
from datetime import datetime, timedelta

robot_date_initial = input().split(';')
robot_db = {}
products_line = deque()
start_time = datetime.strptime(input(), '%H:%M:%S')

for el in robot_date_initial:
    name, process_time = el.split("-")
    robot_db[name] = {'process_time': int(process_time), 'busy_until': start_time}

cur_time = start_time

cmd = input()
while True:
    cur_time = cur_time + timedelta(seconds=1)
    products_line.append(cmd)
    # print(datetime.strftime(cur_time, '%H:%M:%S'))  #  for debugging purposes
    while products_line:
        for key, value in robot_db.items():
            if cur_time > robot_db[key]["busy_until"]:
                print(f"{key} - {products_line.popleft()} [{datetime.strftime(cur_time, '%H:%M:%S')}]")
                robot_db[key]["busy_until"] = cur_time + timedelta(seconds=robot_db[key]['process_time'] - 1)
                if not products_line:
                    break
        else:
            break
    if cmd != "End":
        cmd = input()
    if products_line:
        if products_line[0] == "End":
            break


# print("END____________")   #  for debugging purposes
# print(cur_time)
# print(products_line)
# print(robot_db)
