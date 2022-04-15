import inspect

a = 8
div = []
for i in range(1,a):
    if a%i==0:
        div.append(i)

if sum(div) == a:
    print("Perfect")
else:
    print("not perfecto")

inspect.getfile(sum)





