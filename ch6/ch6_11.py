import random
import turtle
dice = [1,2,3,4,5,6]
distance = random.choice(dice)

one = turtle.Turtle()
one.shape('turtle')
one.color('blue')
one.penup()
one.goto(-100,30)
one.pendown()

two = turtle.Turtle()
two.shape('classic')
two.color('red')
two.penup()
two.goto(-100,-30)
two.pendown()

for i in range(5):
    distance1 = random.choice(dice)
    distance2 = random.choice(dice)
    one.forward(distance1*20)
    two.forward(distance2*20)
turtle.mainloop()
turtle.bye()