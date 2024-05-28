from turtle import *


#we want to paint a house


#step 1: draw a square
speed(10)
width(7)
begin_fill()
color("red")
forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square


#drawing a door

forward(70)
begin_fill()
color("black")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

begin_fill()
color("black")
right(150)
forward(200)
left(120)
forward(200)
color("red")
end_fill()


#drawing a window


color("black")
penup()
goto(150, 160)
pendown()


begin_fill()
right(240)
forward(40)
left(270)
forward(40)
left(270)
forward(40)
left(270)
forward(40)
end_fill()


color("black")
penup()
goto(10, 160)
pendown()

begin_fill()
right(90)
forward(40)
left(270)
forward(40)
left(270)
forward(40)
left(270)
forward(40)
end_fill() 


exitonclick()


