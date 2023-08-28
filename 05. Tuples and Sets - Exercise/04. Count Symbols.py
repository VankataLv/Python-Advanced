txt = input()
symbols = {}
for char in txt:
    if char in symbols:
        symbols[char] += 1
    else:
        symbols[char] = 1

sorted_date = sorted(symbols.items(), key=lambda x: x[0])
for el in sorted_date:
    print(f"{el[0]}: {el[1]} time/s")
