str1 = "Welcome to India. India awesome, isn't it?"
li = list(str1.split())
count = 0
for i in li:
    if "India" in i:
        count+=1

print(count)
