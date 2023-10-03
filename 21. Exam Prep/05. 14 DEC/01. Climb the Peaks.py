from collections import deque

daily_portions = [int(x) for x in input().split(", ")]
daily_stamina = deque([int(x) for x in input().split(", ")])
peaks = deque([("Vihren", 80),
               ("Kutelo", 90),
               ("Banski Suhodol", 100),
               ("Polezhan", 60),
               ("Kamenitza", 70)])
conquered_peaks =[]
for day in range(7):
    cur_portion = daily_portions.pop()
    cur_stamina = daily_stamina.popleft()
    daily_sum = cur_portion + cur_stamina
    if peaks:
        cur_peak = peaks.popleft()
        if daily_sum >= cur_peak[1]:
            conquered_peaks.append(cur_peak[0])
        else:
            peaks.appendleft(cur_peak)

if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print("Conquered peaks:")
    for peak in conquered_peaks:
        print(f"{peak}")
