from turtle import *

# we want to paint a house
#step1: droaw a square


width(7)
color("purple")
begin_fill()

forward (300)
left (90)

forward (300)
left (90)

forward (300)
left (90)

forward (300)
left (90)
end_fill()


#end of the square

#drowing a door

forward (120)

color("yellow")
begin_fill()
left (90)
forward(160)
right (90)
forward (90)
right (90)
forward(160)
right(90)
forward(90)
end_fill()




# we want to draw a window on the right side of the house

penup()
color("red")
speed(50)
begin_fill()
goto(280,180)
pendown()
speed(50)

forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()



#drowing a left window

penup()

color("red")
speed(50)
begin_fill()
goto(110,180)
pendown()

right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()



#drowing a roof

penup()
speed(20)
color("green")
begin_fill()
goto(300,300)
pendown()
right(120)
forward(175)
left(60)
forward(175)
left(150)
forward(305)
end_fill()


#we want to draw a sun

penup()
forward(100)
color("yellow")
speed(2)
pendown()
begin_fill()
circle(50)
end_fill()
exitonclick()




