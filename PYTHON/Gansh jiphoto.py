from turtle import *
title("Ganpati")
bgcolor("white")
color("red")
pensize(5)
speed(5)

left(60)
forward(50)
left(15)
circle(100,90)
forward(30)
pensize(10)
penup()
right(90)
forward(20)
pendown()

right(40)
circle(-50,90)
forward(20)
left(150)

#seconde head curve
color("red")
penup()
forward(40)
left(20)
pendown()
circle(50,90)

#third head curve
color("red")
penup()
goto(0,0)
pensize(5)
pendown()
left(30)
forward(120)
circle(60,270)

#eyes
color("#fc6600")
penup()
forward(30)
right(50)
forward(135)
pendown()
pensize(8)
circle(50,90)
left(95)
penup()
circle(60,75)

#eyebrows
penup()
forward(15)
left(90)
pensize(2)
pendown()
circle(70,90)

#ears
pensize(5)
penup()
forward(75)
right(90)
forward(20)
pendown()
circle(90,90)
forward(20)

circle(30,170)
right(180)
circle(28,180)
right(160)
circle(25,180)
right(160)
circle(22,160)
forward(20)
circle(60,45)

#trunk
penup()
goto(0,0)
left(130)
forward(140)
right(250)
backward(20)
circle(80,20)
circle(20,40)

right(110)
penup()
forward(20)
pendown()
pensize(10)
forward(50)
circle(100,80)
pensize(9)
circle(150,50)
pensize(7)
circle(100,60)
pensize(5)
circle(90,60)
pensize(4)
circle(40,60)
circle(10,90)

#head
color("red")
penup()
goto(0,0)
goto(-90,290)
right(230)
pendown()
circle(-100,50)
circle(200,20)
circle(50,30)
right(180)
circle(50,30)
circle(200,20)
circle(-100,40)
right(95)
penup()
forward(40)
right(90)
pendown()
circle(100,40)
penup()
circle(35,120)
right(30)
pendown()
pensize(1)
circle(60,50)

penup()
goto(-70,90)
fillcolor("red")
begin_fill()
circle(20,180)
end_fill()

penup()
left(75)
fillcolor("red")
begin_fill()
circle(70,35)
end_fill()

left(180)
backward(10)
pendown()
left(6)
pensize(5)
color("red")
circle(-80,40)
penup()
goto(0,0)

write("    Jay Shree Ganesh", font=
("Arial",20,"normal"),align="left")

color("red")
penup()
goto(-250,-60)
left(118)
forward(240)
right(-25)
pendown()
circle(90,65)
penup()
hideturtle()
done()