import turtle
import random

    # Modify the angle used in turning the turtle so that at each branch point
     # the angle is selected at random in some range. For example choose the
     #  angle between 15 and 45 degrees. Play around to see what looks good.
    # Modify the branchLen recursively so that instead of always subtracting
    # the same amount you subtract a random amount in some range.


def tree(branchLen, t):
    if branchLen > 25:
        t.forward(branchLen)
        pensiz = t.pensize()
        t.pensize(0.65 * pensiz)
        rand_ang = random.randrange(15, 46)
        t.right(rand_ang)
        tree(branchLen - random.randrange(3, 8), t)
        t.left(2 * rand_ang)
        tree(branchLen - random.randrange(3, 8), t)
        t.right(rand_ang)
        t.pensize(pensiz)
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.pensize(10)
    # t.up()
    # t.backward(100)
    # t.down()
    t.color("green")
    tree(65, t)
    myWin.exitonclick()

main()
