strg = "my name is is shivam"
str2 = list(strg.split())
lis = []

for i in str2:
    if i not in lis:
        lis.append(i)

print(" ".join(lis))

