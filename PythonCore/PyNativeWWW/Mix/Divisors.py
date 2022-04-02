# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

ask = int(input("Enter a number : "))

li1 = []
for i in range(2,ask+1):
    if i%ask==0:
        li1.append(i)

print(li1)



