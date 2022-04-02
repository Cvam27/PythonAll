word = list(input("Enter a word : "))
print(word)
for i in word:
    count = 0
    for j in word:
        if i == j:
            count = count + 1


    print(i, count)
