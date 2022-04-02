a = 34561
while a>0:
    last_digit = a%10
    a = a//10
    print(last_digit, end=" ")