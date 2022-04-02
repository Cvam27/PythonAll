num = [12,43,23, 67,11,45,54]
max = 0
for i in num:
    for j in num:
        if j>max:
            max = i
        else:
            continue

print(max)