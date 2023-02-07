class Triangle:
    numberOFSides = 3

    def __init__(self,a1,a2,a3):
        self.angle1 = a1
        self.angle2 = a2
        self.angle3 = a3

    def __str__(self):
        return f"삼각형 각도 {self.angle1} {self.angle2} {self.angle3}"

    def setAngle1(self,a1):
        self.angle1 = a1

    def setAngle2(self,a2):
        self.angle2 = a2

    def setAngle3(self,a3):
        self.angle3= a3

    def getAngle1(self):
        return self.angle1

    def getAngle2(self):
        return self.angle2

    def getAngle3(self):
        return self.angle3

    def checkingAngle(self):
        if self.angle1+self.angle2+self.angle3 == 180:
            return True
        else:
            return False

triangle = Triangle(90,30,60)
print(triangle.checkingAngle())