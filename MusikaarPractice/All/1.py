'''
1.	Write a program which accepts a number as an argument and prints an ascending triangle pattern containing character ‘*’. For example output of function pattern(5) should be following,
   *
  * *
 * * *


'''

# for i in range(5,0,-1):
#     for j in range(i//2,0,-1 ):
#         print(" ", end="")
#     for star in range(i, 6, 1):
#         print("*", end="")
#     print("")

for i in range(6,0,-1):
    for j in range(i//2,0,-1 ):
        print(".", end="")
    for star in range(i, 6, 1):
        print("*", end="")
    print("")

# i=5
# while i !=0:
#     for j in range(i-1,0,-1 ):
#         print("_", end="")
#     for star in range(i, 5, 1):
#         print("*", end="")
#     print("")
#     i=i-1


