def outer_func(a,b):
    def inner_func():
        summ = a+b
        return summ
    return inner_func() + 5
print(outer_func(5,7))


