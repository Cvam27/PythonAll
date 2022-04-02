list1 = [5, 20, 15, 20, 25, 50, 20]
#
# for i in list1:
#     if i == 20:
#         list1.remove(i)
#
#
# print(list1)

len1 = len(list1)
for i in range(len1):
    if list1[i] == 20:
        list1.pop(list1[i])


print(list1)