import turtle
t = turtle.Turtle()
t.shape("classic")
alist = [i for i in range(10,130,10)]
for i in alist:
    t.forward(i)
    t.stamp()
    t.backward(i)
    t.right(30)

turtle.mainloop()
turtle.bye()