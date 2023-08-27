num_guests = int(input())
vip_guests = set()
regular_guests = set()

for _ in range(num_guests):
    cur_rsv = input()
    if cur_rsv[0].isdigit():
        vip_guests.add(cur_rsv)
    else:
        regular_guests.add(cur_rsv)

cmd = input()
while cmd != "END":
    if cmd in vip_guests:
        vip_guests.remove(cmd)
    elif cmd in regular_guests:
        regular_guests.remove(cmd)
    cmd = input()

no_show_guests = (vip_guests | regular_guests)
print(len(no_show_guests))

for guest in sorted(no_show_guests):
    print(guest)

# 5
# 7IK9Yo0h
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# tSzE5t0p
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# END