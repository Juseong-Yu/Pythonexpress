import turtle
import random
t = turtle.Turtle()
t.shape('turtle')

def draw_square(x,y,c):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(c) 
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()

for c in ['yellow','red','purple','blue']:
    draw_square(random.randint(-50,50),random.randint(-50,50),c)
