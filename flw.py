import turtle

li = turtle.Turtle()
li.screen.bgcolor("black")
li.pensize(2)
li.color("green")
li.left(90)
li.backward(60)
li.speed(50000)
li.shape("turtle")

def love(i):
    if i<10:
        return
    else:
        li.forward(i)
        li.color("purple")
        li.circle(2)
        li.color("green")
        li.left(30)

        love(5*i/6)

        li.right(60)

        love(5*i/6)

        li.left(30)
        li.backward(i)
love(60)
turtle.done()       