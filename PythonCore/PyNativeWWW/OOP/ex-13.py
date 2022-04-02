class Computation:
    def __init__(self):
        pass

    def Factorial(self,x):
        fact=1
        for i in range(1,x):
            fact = fact*i
        return fact

    def Sum(self,y):
        sum =0
        for i in range(1,y):
            sum = sum + i
        return sum

    def testPrime(self, prim):
        for i in range(2,prim//2):
            if prim%i==0:
                print("Number is not prime")
                break
        else:
            print("Number is prime")

    def testPrimes(self, start, end):
        for i in range(start, end+1):
            for j in range(2,i//2):
                if i%j==0:
                    break
            else:
                print(i, "is prime")

    def tableMulti(self, num):
        self.num = num
        for i in range(1,11):
            print(num*i)

    def allTableMulti(self, num1):
        self.num1 = num1
        for i in range(1,10):
            for j in range(1,11):
                print(i*j, end=" ")
            print("")



O = Computation()
O.allTableMulti(10)
