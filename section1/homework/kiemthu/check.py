import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("green")

tess.penup()
size = 20
for i in range (20) :
    tess.stamp()
    size = size + 3
    tess.forward(size)
    tess.right(24)

wn.mainloop()    