class PhoneBook:
    def __init__(self):
        self.Dict={}

    def add(self,name,mobile=None,office=None,email=None):
        self.Dict.update({name : [mobile,office,email]})

    def __str__(self):
        str1 = ""
        for key in self.Dict.keys():
            str1 += key+"\n"
            for i in range(len(self.Dict[key])):
                if self.Dict[key][i] != None:
                    if i == 0:
                        str1 +="mobile:  "+self.Dict[key][i]+"\n"
                    elif i == 1:
                        str1 +="office phone:  "+self.Dict[key][i]+"\n"
                    elif i == 2:
                        str1 +="email adress:  "+self.Dict[key][i]+"\n"
        return str1

obj = PhoneBook()
obj.add("Kim", office= "1234567",email= "kim@company.com")
obj.add("Park",office="2345678",email= "park@company.com")

print(obj)