import turtle

t = turtle.Turtle()
b = turtle.Screen()
b.bgcolor("black")
t.left(90)
t.hideturtle()

t.speed()
t.pensize(3)
t.color("brown")

t.speed(0)


def tree(i):
    if i < 10:
        return

    else:
        t.forward(i)
        t.color("pink")
        t.circle(2)
        t.color("brown")
        t.left(30)
        tree(3 * i / 4)
        t.right(60)
        tree(3 * i / 4)
        t.left(30)
        if i == 100:
            t.color("brown")
        else:
            t.color("brown")
        t.backward(i)



tree(100)

t.color("pink")
t.penup()
t.goto(-140, -100)
t.pendown()
t.write("Tree of Recursion", font=("Verdana", 25, "normal"))
turtle.done()
