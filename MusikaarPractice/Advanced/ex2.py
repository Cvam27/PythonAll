#this is decorator function
def deco(name_decorator):
    return name_decorator.upper()

def main_func(func):
    name_modifier = func("Testing")
    print(name_modifier)

main_func(deco)
