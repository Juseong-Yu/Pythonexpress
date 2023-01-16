import turtle
t = turtle.Turtle()
t.shape("turtle")

h = turtle.Turtle()
h.hideturtle() 

def draw_line():
    h.forward(100)
    h.backward(100)
    h.left(30)

for i in range(12):
    draw_line()
    t.left(30)


turtle.mainloop()
turtle.bye()