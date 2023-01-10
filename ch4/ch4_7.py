import turtle
import math

t = turtle.Turtle()
t.shape('turtle')

for i in range (360):
    t.goto(i,math.sin(math.pi*i/180)*100)

turtle.mainloop()
turtle.bye()