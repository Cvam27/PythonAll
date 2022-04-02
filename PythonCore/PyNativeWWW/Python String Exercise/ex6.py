# s1 = "Abc"
# s2 = "Xyz"
#
# x1 = len(s1)//2
# mid1 = s1[x1:x1+1]
#
# x2 = len(s2)//2
# mid2 = s2[x2:x2+1]
#
# res = s1[0] + s2[-1] + mid1 + mid2 + s1[-1] + s2[0]
# print(res)

#Approach 2-------------
s1 = "Abcd"
s2 = "Wxyz"

# get string length
s1_length = len(s1)
s2_length = len(s2)

# get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
result = ""

# reverse s2
s2 = s2[::-1]

# iterate string
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)
