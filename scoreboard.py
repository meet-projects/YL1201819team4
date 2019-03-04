import turtle
from turtle import Turtle
import time
turtle.addshape("gold.gif")
def show_scoreboard(A_points, B_points, C_points, D_points, finnished):
    headline = turtle.clone()
    turtle.hideturtle()
    headline.hideturtle()
    headline.penup()
    headline.goto(0,300)
    headline.color("black")
    headline.write("SCOREBOARD", align = "center", font=("Comic Sans MS", 100, "bold"))

    A = turtle.clone()
    turtle.hideturtle()
    A.hideturtle()
    A.penup()
    A.goto(-400,100)
    A.color("red")
    A.write("PLAYER A - 'Q'", align = "center", font=("Comic Sans MS", 40, "bold"))
    A.goto(-400,-30)
    A.color("grey")
    A.write(str(A_points), align = "center", font=("Comic Sans MS", 50, "bold"))

    B = turtle.clone()
    turtle.hideturtle()
    B.hideturtle()
    B.penup()
    B.goto(400,100)
    B.color("blue")
    B.write("PLAYER B - 'C'", align = "center", font=("Comic Sans MS", 40, "bold"))
    B.goto(400,-30)
    B.color("grey")
    B.write(str(B_points), align = "center", font=("Comic Sans MS", 50, "bold"))

    C = turtle.clone()
    turtle.hideturtle()
    C.hideturtle()
    C.penup()
    C.goto(-400,-200)
    C.color("yellow")
    C.write("PLAYER C - 'M'", align = "center", font=("Comic Sans MS", 40, "bold"))
    C.goto(-400,-330)
    C.color("grey")
    C.write(str(C_points), align = "center", font=("Comic Sans MS", 50, "bold"))

    D = turtle.clone()
    turtle.hideturtle()
    D.hideturtle()
    D.penup()
    D.goto(400,-200)
    D.color("green")
    D.write("PLAYER D - 'P'", align = "center", font=("Comic Sans MS", 40, "bold"))
    D.goto(400,-330)
    D.color("grey")
    D.write(str(D_points), align = "center", font=("Comic Sans MS", 50, "bold"))

    pointsList = [A_points, B_points, C_points, D_points]

    if finnished:
        time.sleep(2)
        turtle.clearscreen()
        winners = [0, 0, 0, 0]
        maxV = 0
        counter = 0
        for i in pointsList:
            if maxV < i:
                maxV = i

        for i in range(len(pointsList)):
            if pointsList[i] == maxV:
                if i == 0:
                    wColor = "red"
                    wName = "PLAYER A"
                elif i == 1:
                    wColor  = "blue"
                    wName = "PLAYER B"
                elif i == 2:
                    wColor  = "yellow"
                    wName = "PLAYER C"
                elif i == 3:
                    wColor  = "green"
                    wName = "PLAYER D"


        winT = turtle.clone()
        turtle.hideturtle()
        winT.hideturtle()
        winT.penup()
        winT.goto(0,0)
        winT.color(wColor)
        winT.write("THE WINNER IS " + wName, align = "center", font=("Comic Sans MS", 80, "bold"))
        winT.shape("gold.gif")
        winT.goto(0, -150)
        winT.showturtle()
    time.sleep(5)

