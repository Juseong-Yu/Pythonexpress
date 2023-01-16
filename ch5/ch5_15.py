import turtle
t = turtle.Turtle()
t.shape("turtle")

def draw_square(size):
    for i in range(50):
        t.fd(size)
        t.left(90)
        size = size + 5

draw_square(10)

turtle.mainloop()
turtle.bye()