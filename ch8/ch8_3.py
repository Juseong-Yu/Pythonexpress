class Box:
    def __init__(self,l,h,d):
        self.length = l
        self.height = h
        self.depth = d

    def __str__(self):
        return f"({self.length}, {self.height}, {self.depth})"

    def setLength(self,l):
        self.length = l

    def getLength(self):
        return self.length

    def setHeight(self,h):
        self.height = h

    def getHeight(self):
        return self.height

    def setDepth(self,d):
        self.depth = d

    def getDepth(self):
        return self.depth

b1 = Box(100,100,100)
print(b1)
print("상자의 부피는",b1.getHeight()*b1.getLength()*b1.getDepth())