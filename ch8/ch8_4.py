class Rectangle:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        return f"좌표 : {self.x} {self.y} 크기 : ",self.width*self.height

    def setX(self,x):
        self.x = x
    
    def getX(self):
        return self.x

    def setY(self,y):
        self.y = y

    def getY(self):
        return self.y

    def getArea(self):
        return self.width*self.height
    
    def overlap(self,r):
        if (self.x+self.width < r.x or r.x+r.width < self.x) or (self.y+self.height < r.y or r.y+r.height < self.y):
            return False
        else:
            return True

r1  = Rectangle(0,0,100,100)
r2 = Rectangle(10,10,100,100)
print(r1.overlap(r2))