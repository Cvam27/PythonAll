with open('test.txt', 'r') as rf:
    with open('test2.txt', 'w') as wf:
        for i in rf:
            wf.write(i)


print("done")

