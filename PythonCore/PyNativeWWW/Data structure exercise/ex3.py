sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

len1 = int(len(sample_list)/3)

l1 = sample_list[0:(len1)]
l2 = sample_list[(len1) : (len1*2)]
l3 = sample_list[(len1*2): ]

print(l1, l2, l3)
print(l1[::-1])
print(l2[::-1])
print(l3[::-1])