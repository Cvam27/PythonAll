
try:
    user_age = int(input("Enter age : "))
    user_gender = input("Enter gender : ")
    user_family_member = int(input("Enter family member count: "))
    if user_age >= 25 and user_gender == "male" and user_family_member < 5:
        print("Offer applicable")
    else :
        f= open('a.txt','r')

except ValueError:
    print("Please enter valid info")
except FileNotFoundError:
    print("Are bhai bhai bhai")