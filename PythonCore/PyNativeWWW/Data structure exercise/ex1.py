l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28, 45]
# len1 = len(l1)
# len2 = len(l2)
l3= []
# len = len1 if len1>len2 else len2
#
# for i in range(0,len):
#     if i%2==0:
#         l3.append(l2[i])
#     else:
#         l3.append(l1[i])

# print(l3)

lt1 = l1[1::2]
lt2 = l2[0::2]

lt3 = lt1 + lt2
print(lt3)
