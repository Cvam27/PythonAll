li1 = []
li2 = [27,15,12,9]
li3 = []
for i in range(50):
    if i%3 == 0:
        li1.append(i)
    elif i%5==0:
        li2.append(i)

set1 = set(li1)
set2 = set(li2)
set3 = set(li3)
for k in set1:
    for j in set2:
        if i==j:
         li3.append(i)

print(set3)