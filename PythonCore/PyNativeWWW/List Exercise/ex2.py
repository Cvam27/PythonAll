list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

len1 = len(list1)
len2 = len(list2)
new_list = []

for i in range(len1) and range(len2):
    new_list.append(list1[i] + list2[i])

print(new_list)