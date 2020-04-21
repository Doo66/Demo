val = 0
while val < 100:
    val += 1
    if val % 7 == 0 or val % 10 == 7 or val // 10 == 7:
        continue
    else:
        print(val)
