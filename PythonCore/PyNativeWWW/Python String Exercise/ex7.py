s1 = "Yn"
s2 = "PYnative"

def string_check(s1, s2):
    flag = True
    for i in s1:
        if s2.__contains__(i):
            pass
        else:
            flag = False
    return flag


print(string_check(s1, s2))

