word = list(input("Enter a word : "))
print(word)
li1 = []
for i in word:
    count = 0
    for j in word:
        if i == j:
            count = count + 1

        if count != 0:
            print(i, "is", count, "times")
        else:
            count +=1
