# str1 = "Apple"
# di1 = {}
# for i in str1:
#     count = str1.count(i)
#     di1[i] = count
#
# print(di1)

#Approach 2

str1 = "Apple"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict, type(char_dict))
