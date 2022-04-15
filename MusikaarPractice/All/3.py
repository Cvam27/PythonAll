name = str(input("Enter string: "))
split_name = name.split()
cap_name = []
for i in split_name:
    cap_name.append(i.capitalize())
print(" ". join(cap_name[::-1]))
