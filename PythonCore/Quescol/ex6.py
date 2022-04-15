def max(n):
    lst = []
    for i in range(1,n+1):
        num = int(input(f"Enter {i} number: "))
        lst.append(num)

    max_num = 0
    for i in lst:
        if i > 0:
            max_num = i
    return print("Biggest numer is : ", max_num)

max(5)