sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict = {}
#
# for i in sample_list:
#     count = 0
#     for j in range(0,len(sample_list)):
#         if sample_list[j]==i:
#             count +=1
#         dict[i]=count
#
# print(dict)


for i in sample_list:
    count = 0
    for j in sample_list:
        if j==i:
            count +=1
        dict[i]=count

print(dict)

#Approach 2
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)
