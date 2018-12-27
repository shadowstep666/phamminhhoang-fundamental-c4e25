from turtle import *

color("red")

begin_fill()
shape("arrow")

right(30)
for i in range(16) :
    forward(100)
    left(60)
    forward(100)
    left(120)
    forward(100)
    left(60)
    forward(100)
    left(150)


mainloop()