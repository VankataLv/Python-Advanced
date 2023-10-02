from collections import deque

time_to_complete_task = deque([int(x) for x in input().split()])
number_tasks = [int(x) for x in input().split()]
duck_db = {"Vader": 0,
           "Thor": 0,
           "Blue": 0,
           "Yellow": 0}

while len(time_to_complete_task) > 0 and len(number_tasks) > 0:
    cur_time = time_to_complete_task.popleft()
    cur_task = number_tasks.pop()
    product = cur_time * cur_task
    if product in range(0, 61):
        duck_db["Vader"] += 1
    elif product in range(61, 121):
        duck_db["Thor"] += 1
    elif product in range(121, 181):
        duck_db["Blue"] += 1
    elif product in range(181, 241):
        duck_db["Yellow"] += 1
    else:
        cur_task -= 2
        time_to_complete_task.append(cur_time)
        number_tasks.append(cur_task)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {duck_db['Vader']}")
print(f"Thor Ducky: {duck_db['Thor']}")
print(f"Big Blue Rubber Ducky: {duck_db['Blue']}")
print(f"Small Yellow Rubber Ducky: {duck_db['Yellow']}")
