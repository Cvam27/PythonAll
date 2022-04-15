with open("f1.txt","w") as f:
    f.write("Test1, test2, testtttt")

with open("f1.txt", "r") as f:
    spl = f.read()
    perword = spl.split()
    print(len(perword))