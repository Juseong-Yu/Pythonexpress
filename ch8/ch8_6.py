class Person:
    def __init__(self,n=None,m=None,o=None,e=None):
        self.name = n
        self.mobile = m
        self.office = o
        self.email = e

    def __str__(self):
        return f"{self.name} {self.mobile} {self.office} {self.email}"
        
    def setName(self,n):
        self.name = n

    def getName(self):
        return self.name

    def setmobile(self,m):
        self.mobile = m

    def getmobile(self):
        return self.mobile

    def setoffice(self,o):
        self.office= o

    def getoffice(self):
        return self.office

    def setemail(self,e):
        self.email = e

    def getemail(self):
        return self.email

p1 = Person("Kim", o = "1234567",e = "kim@company.com")
p2 = Person("Park",o="2345678")
p2.setemail("park@comapny.com")
print(p1)
print(p2)