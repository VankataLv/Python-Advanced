from collections import deque
from datetime import datetime, timedelta

robot_date_initial = input().split(';')
robot_db = deque()
products_line = deque()
start_time = datetime.strptime(input(), '%H:%M:%S')
start_time = start_time.time()

for el in robot_date_initial:
    name, process_time = el.split("-")
    robot = {'name': name, 'process_time': int(process_time), 'busy_until': start_time}
    robot_db.append(robot)

cur_time = datetime(start_time)
cmd = input()
while cmd != "End":
    cur_time = cur_time + timedelta(seconds=1)
    products_line.append(cmd)
    while products_line:
        for robot in robot_db:
            if cur_time > robot["busy_until"]:

                print(f"{robot['name']} - {products_line.popleft()} [{cur_time}]")
            else:
                continue

    cmd = input()

print("END____________")
