def remove_char():
    word = input("Enter a word")
    crop = int(input("how many to crop : "))


    cropped = word[crop:]
    return cropped


print(remove_char())