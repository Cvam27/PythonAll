str1 = "e29@#8496"
Sum = 0
count = 0
for i in str1:
    if i.isdigit() == True:
        Sum =Sum + int(i)
        count = count + 1


print("Sum is : ", Sum)
avg = Sum/count
print("Avg is : ", avg)