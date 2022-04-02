list1 = [54, 44, 27, 79, 91, 41]
len1 = len(list1)
popped = list1.pop(4)
print(list1)
list1.append(popped)
list1.insert(1,popped)
print(list1)