str1 = "Emma is a data scientist who knows Python. Emma works at google."
str_split = str1.split()
size = len(str1)

for i in str_split:
    if i == "Emma":
        print(str_split.index('Emma'))
