'''
1
2 3
4 5 6
7 8 9 10'''
col = 1
for column in range(1, 5):
    for row in range(1, column + 1):
        print(col, end=" ")
        col += 1
    print("")
