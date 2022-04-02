class p1:
    def string_one(self, str1):
        self.str1 = str1

    def show_string_one(self):
        print("from string1")
        return self.str1

class p2:
    def string_two(self, str2):

        self.str2 = str2

    def show_string_two(self):
        print("from string2")
        return self.str2

class c1(p1, p2):
    def strinf_three(self, str3):
        self.str3 = str3

    def show_string_three(self):
        print("from string3")
        return self.str3


kid = c1()
kid.string_one("string 1")
kid.string_two("string 2")
kid.strinf_three("String 3")

kid.show_string_one(),kid.show_string_two(),kid.show_string_three()
