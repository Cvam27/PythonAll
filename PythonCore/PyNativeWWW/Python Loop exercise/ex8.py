list1 = [10, 20, 30, 40, 50]
new_list = reversed(list1)

#Approach 1
# for i in new_list:
#     print(i)

#Approach 2
for i in range(len(list1)-1,-1,-1):
    print(list1[i])