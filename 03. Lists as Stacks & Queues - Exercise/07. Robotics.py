from collections import deque
from datetime import datetime, timedelta


class Robot:
    def __init__(self, name, process_time):
        self.name = name
        self.work_cap = int(process_time)
        self.busy_until = None

    def __str__(self):
        return f"{self.name}-{self.work_cap}busy until:{self.busy_until}"

    def is_free(self, current_time):
        if self.busy_until is None or current_time >= self.busy_until:
            return True
        else:
            return False

    def start_processing(self, product, current_time):
        self.busy_until = current_time + timedelta(seconds=self.work_cap)
        print(f"{self.name} - {product} [{current_time.strftime('%H:%M:%S')}]")


free_robots = deque()
robot_data = input().split(";")
for robot in robot_data:
    name, process_time = robot.split("-")
    process_time = int(process_time)
    free_robots.append(Robot(name, process_time))


start_time = datetime.strptime(input(), "%H:%M:%S")
product_line = deque()
cmd = input()
current_time = start_time

while True:
    current_time += timedelta(seconds=1)
    product_line.append(cmd)
    for robot in free_robots:
        if not robot.busy_until:
            robot.busy_until = True
            print(f"{robot.name} - {product_line.popleft()} [{current_time.strftime('%H:%M:%S')}]")
            for robot in free_robots:
                print(robot)
            break
    cmd = input()



