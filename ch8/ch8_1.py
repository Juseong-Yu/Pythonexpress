class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'

    def setName(self,name):
        self.name = name
    
    def getName(self):
        return self.name

missy = Cat('missy',3)
lucky = Cat('lucky',5)

print(missy)
print(lucky)

lucky.setName('lucifer')
print(lucky.getName())