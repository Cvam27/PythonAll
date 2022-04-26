import random

a = ["[","]"]
for i in range(10):
    shuffle = random.choice(a)
    print(shuffle, end="")

for j in range(len(shuffle)):
    if shuffle[j] =="[":
        if shuffle[j] == "]":
            pass
        else:
            print("Not OK")
    print("OK")
# open = 0
# close = 0
# for i in shuffle:
#     if i == "[":
#         open = open+1
#     elif i == "]":
#         close = close +1
#
# print(open, close)