import turtle

class Turtle_new(turtle.Turtle):
    def move(self,angle = 0):
        if angle != 0:
            self.right(angle)
        self.forward(100)
        self.right(90)
        self.forward(30)
        self.left(90)
        self.forward(100)

lee = Turtle_new("turtle")
kim = Turtle_new("circle")
lee.move()
kim.move(180)


turtle.exitonclick()