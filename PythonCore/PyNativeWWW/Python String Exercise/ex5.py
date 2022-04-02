str1 = "P@#yn26at^&i5ve"
char=[]
digit=[]
symbol=[]
for i in str1:
    if i.isalpha() == True:
        char.append(i)
    elif i.isdigit()== True:
        digit.append(i)
    else:
        symbol.append(i)

char=len(char)
digit=len(digit)
symbol=len(symbol)

print("Char: ",char)
print("digit: ",digit)
print("symbol: ",symbol)