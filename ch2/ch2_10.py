import turtle
t = turtle.Turtle()
t.shape('turtle')

side = int(input('변 길이'))
t.fd(side)
t.left(120)
t.fd(side)
t.left(120)
t.fd(side)

turtle.mainloop()
turtle.bye()