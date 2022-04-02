a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# new_a=[]
# for i in a:
#     if i <5:
#         new_a.append(i)
#     else:
#         pass
#
# print(new_a)
#
# print([i for i in a if i<5])

ask = int(input("Enter a number : "))

for i in a:
    if i < ask:
        print(i)
    else:
        pass

