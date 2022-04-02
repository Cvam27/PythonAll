li1 = [22, 3, 554, 15, 23, 11, 1010, 12, 4, 26, 80, 121, 2020]
len1 = len(li1)
new = []
for i in range(len1):
    if li1[i] > li1[i+1]:
        new.append(li1[i])

print()