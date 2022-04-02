list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

len1 = len(list1)
len2 = len(list2)

new_li = []

for i in range(len1):
    for j in range(len2):
        new_li.append((list1[i]+list2[j]))

print(new_li)