num = int(input("Enter num for factorial : "))
fact = 1
for i in range(num,1, -1):
    fact = fact*(i)

print(fact)
