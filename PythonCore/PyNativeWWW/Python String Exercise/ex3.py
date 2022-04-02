s1 = "America"
s2 = "Japan"

x1 = len(s1)//2
mid1 = s1[x1:x1+1]

x2 = len(s2)//2
mid2 = s2[x2:x2+1]

result = s1[0]+ s2[0] +mid1 + mid2 + s1[-1] + s2[-1]

print(result)