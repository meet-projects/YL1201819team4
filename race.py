import turtle
from turtle import Turtle
import time

turtle.addshape('boat 1.gif')

additions = [0, 0, 0, 0]
RUNNING = True
def play_race():
    turtle.bgpic("sea.gif")
    global END, additions, RESUMrfE
    END = False
    class Player(Turtle):
        def __init__(self, y, color, name, index, ball):
            Turtle.__init__(self)
            self.shape('boat 1.gif')
            ball.shapesize(3)
            ball.color(color)
            self.penup()
            ball.penup()
            ball.showturtle()
            ball.goto(-780, y)
            self.goto(-700, y)
            self.name = name
            self.index = index
            self.ball = ball
            self.color = color

        def move(self):
            global END
            if not END:
                self.forward(10)
                self.ball.forward(10)
                if self.xcor() > 700:
                    END = True
                    endGame(self)
                    
        def getColor(self):
            currentColor = self.color
            return(currentColor)
        def getName(self):
            name = self.name
            return(name)
        def getIndex(self):
            index = self.index
            return(index)

        def printAdd():
            print(additions)

    #HEADLINE SETUP
    headline1 = turtle.clone()
    turtle.hideturtle()
    headline1.hideturtle()
    headline1.penup()
    headline1.goto(0,350)
    headline1.color("black")
    headline1.write("RACE", align = "center", font=("Comic Sans MS", 50, "bold"))

    #FINISH LINE
    fLine = turtle.clone()
    fLine.hideturtle()
    fLine.penup()
    fLine.color("grey")
    fLine.goto(700,320)
    fLine.pendown()
    fLine.pensize(20)
    fLine.goto(700,-480)

    #END SETUP
    def endGame(player):
        global RUNNING
        turtle.clearscreen()
        bg = player.getColor()
        turtle.bgcolor(bg)
        winner = player.getName()
        headline1.goto(0,200)
        headline1.color("white")
        headline1.write("THE WINNER IS", align = "center", font=("Comic Sans MS", 90, "bold"))
        headline1.goto(0,50)
        headline1.write(winner, align = "center", font=("Comic Sans MS", 90, "bold"))

        additions[player.getIndex()] += 100
        RUNNING = False

    c1 = turtle.clone()
    p1 = Player(200,"red", "PLAYER A", 0, c1)
    c2 = turtle.clone()
    p2 = Player(0,"blue", "PLAYER B", 1, c2)
    c3 = turtle.clone()
    p3 = Player(-200,"yellow", "PLAYER C", 2, c3)
    c4 = turtle.clone()
    p4 = Player(-400,"green", "PLAYER D", 3, c4)
    
    players = [p1, p2, p3, p4]

    turtle.onkey(p1.move, "q")
    turtle.onkey(p2.move, "c")
    turtle.onkey(p3.move, "m")
    turtle.onkey(p4.move, "p")
    turtle.listen()
    while RUNNING:
        turtle.update()
    time.sleep(3)

    """penDown = True
                def penChange:
                    if penDown:
                        fLine.penup()
                    elif not penDown:
                        fLine.pendown()
                for i in range(16)"""
