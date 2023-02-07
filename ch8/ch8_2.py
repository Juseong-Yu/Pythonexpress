class Rocket:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"로켓의 위치 {self.x} {self.y}"

    def moveUp(self):
        self.y += 1

myRocket = Rocket()
print("로켓의 높이: ",myRocket.y)

myRocket.moveUp()
print("로켓의 높이: ",myRocket.y)