# def recursive():
#     a=0
#     for i in range(0,11):
#         sum = a+i
#         a=sum
#
#     print(a)
#
# recursive()

def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)


