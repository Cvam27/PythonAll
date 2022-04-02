income = int(input("Enter salary :"))

if income <= 10000:
    tax = 0
elif income >10000 and income <=20000:
    tax = (income-10000)*0.1
else:
    tax = (10000*0.1)+ (income-20000)*0.2

print("Income of the client is:",income)
print("Tax on the given income is:",tax)
