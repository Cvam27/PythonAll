# Fibonacci with Recursion
a = 0
b = 1


#
#
# def rec(n):
#     if n <= 1:
#         return n
#     else:
#         return rec(n - 1) + rec(n - 2)
#
#
# for i in range(10):
#     print(rec(i))

# Fibonacci with Generator

def gen(n):
    global a, b
    yield print(a)
    yield print(b)

    if n <= 1:
        yield n
        n - 1
    else:
        for i in range(n):
            fib = a + b
            a = b
            b = fib
            yield print(fib)


list(gen(10))
