from functools import reduce

total = sum(map(lambda x: x ** 3, filter(lambda y: y % 2 != 0, range(0, 300))))


print(total)
