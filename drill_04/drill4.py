import turtle

turtle.forward(500)

count = 0
while(count < 6):
    turtle.penup()
    turtle.goto(0,count*100)
    turtle.pendown()
    turtle.forward(500)
    count = count + 1


turtle.penup()
turtle.goto(0,500)
turtle.right(90)

count = 0
while(count < 6):
    turtle.penup()
    turtle.goto(count*100,500)
    turtle.pendown()
    turtle.forward(500)
    count = count + 1
