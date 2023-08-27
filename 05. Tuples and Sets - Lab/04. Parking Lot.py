num_cmds = int(input())
car_db = set()

for _ in range(num_cmds):
    direction, licence_plate = input().split(", ")
    if direction == "IN":
        car_db.add(licence_plate)
    else:
        car_db.remove(licence_plate)

if car_db:
    for car in car_db:
        print(car)
else:
    print("Parking Lot is Empty")
# 4
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# OUT, CA1234TA

# 10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU