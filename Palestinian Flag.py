#First import turtle and all its functions 
from turtle import *
speed(10)
setup (800,500)

penup()
goto(-400,250)
pendown()

#black strip
color('black')
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

left(90)

#white strip 
color("white")
begin_fill()
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()

left(180)
penup()
forward(167)
pendown()

#green strip
color('green')
begin_fill()
forward(167)
right(90)
forward(800)
right(90)
forward(167)
end_fill()

#red triangle
left(180)
penup()
goto(-400,250)
pendown()

color('red')
begin_fill()
forward (500)
left(130)
forward(400)
end_fill()

hideturtle()