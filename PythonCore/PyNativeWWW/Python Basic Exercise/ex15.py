def exponent(base, exp):
    # total = pow(base, exp)
    # return  total
    multi = 1
    for i in range(exp):
        multi = base * multi
    return multi


sum = exponent(2,4)
print(sum)
