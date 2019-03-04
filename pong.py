import turtle
import random
import time
from turtle import Turtle
from turtle import Screen

POINTS = [0, 0]

def play_pong():
	turtle.bgpic("pongbg.gif")
	global POINTS

	turtle.tracer(0)
	SLEEP = 0.0077

	SCREEN_WIDTH = turtle.getcanvas().winfo_width()//2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()//2

	RACKET_WIDTH = 20
	RACKET_LENGTH = 160

	LEFT = 0
	RIGHT = 1

	BOTTOM_RACKET = 5
	UPPER_RACKET = 35

	RUNNING = True

	turtle.penup()
	turtle.hideturtle()
	turtle.home()
	turtle.begin_poly()
	turtle.fd(RACKET_LENGTH)
	turtle.left(90)
	turtle.fd(RACKET_WIDTH)
	turtle.left(90)
	turtle.fd(RACKET_LENGTH)
	turtle.left(90)
	turtle.fd(RACKET_WIDTH)

	turtle.end_poly()

	rec = turtle.get_poly()
	turtle.register_shape("racket", rec)

	score = turtle.Turtle()
	score.hideturtle()
	score.penup()

	headline1 = turtle.clone()
	turtle.hideturtle()
	headline1.hideturtle()
	headline1.penup()
	headline1.goto(0,350)
	headline1.color("black")
	headline1.write("PONG", align = "center", font=("Comic Sans MS", 50, "bold"))



	class Ball(Turtle):
		def __init__(self, dx, dy, dirc):
			Turtle.__init__(self)
			self.shape("circle")
			self.shapesize(1)
			self.penup()

			self.dx = dx
			self.dy = dy
			self.dirc = dirc
		
		def move(self):
			self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
			for i in RACKETS:
				if collide(i):
					if self.dirc == RIGHT:
						self.dirc = LEFT
					else:
						self.dirc = RIGHT
					self.dy = -self.dy
					self.dy += random.randint(-1, 1)
					self.dx = -self.dx
					self.dx += random.randint(-1, 1)
					while self.dx <= 2 and self.dx >= -2:
						self.dx += random.randint(-1, 1)
					return 0
			if (self.xcor() >= SCREEN_WIDTH):
				POINTS[LEFT] += 25
				self.goto(0, 0)
				self.dx = random.randint(-3, 3)
				self.dy = random.randint(-3, 3)
				while self.dx >= -2 and self.dx <= 2:
					self.dx = random.randint(-3, 3)

				score.clear()
				score.goto(-20, SCREEN_HEIGHT - 65)
				score.write(POINTS[0]//25, align = "center", font = ("Ariel", 20, "normal"))
				score.goto(20, SCREEN_HEIGHT - 65)
				score.write(POINTS[1]//25, align = "center", font = ("Ariel", 20, "normal"))

				return 0

			elif (self.xcor() <= -SCREEN_WIDTH):
				POINTS[RIGHT] += 25
				self.goto(0, 0)
				self.dx = random.randint(-3, 3)
				self.dy = random.randint(-3, 3)
				while self.dx >= -2 and self.dx <= 2:
					self.dx = random.randint(-3, 3)

				score.clear()
				score.goto(-20, SCREEN_HEIGHT - 40)
				score.write(POINTS[0]//25, align = "center", font = ("Ariel", 20, "normal"))
				score.goto(20, SCREEN_HEIGHT - 40)
				score.write(POINTS[1]//25, align = "center", font = ("Ariel", 20, "normal"))

				return 0

			if (self.ycor() >= SCREEN_HEIGHT or self.ycor() <= -SCREEN_HEIGHT):
				self.dy = -self.dy

	class Racket(Turtle):
		def __init__(self, color, index, side, space, dirc):
			Turtle.__init__(self)
			self.penup()
			self.shape("racket")
			self.color(color)
			self.dirc = dirc
			self.space = space
			self.side = side
			if side == LEFT:
				self.setx(space - SCREEN_WIDTH)
			elif side == RIGHT:
				self.setx(SCREEN_WIDTH - space)

		def move(self):
			if not ((self.ycor() + self.dirc) + RACKET_WIDTH//2 >= SCREEN_HEIGHT or (self.ycor() + self.dirc) - RACKET_WIDTH//2 <= -SCREEN_HEIGHT):
				self.sety(self.ycor() + self.dirc)

		def changeDir(self):
			self.dirc = -self.dirc

	def collide(racket):
		if ((ball.ycor() >= racket.ycor() - RACKET_LENGTH) and (ball.ycor() <= racket.ycor())):
			if(racket.space == BOTTOM_RACKET and (racket.side == LEFT and ball.xcor() <= -SCREEN_WIDTH + BOTTOM_RACKET + RACKET_WIDTH and ball.dirc == LEFT) or (racket.side == RIGHT and ball.xcor() >= SCREEN_WIDTH - BOTTOM_RACKET - 10 and ball.dirc == RIGHT)):
				return True
			if(racket.space == UPPER_RACKET and (racket.side == LEFT and ball.xcor() <= -SCREEN_WIDTH + UPPER_RACKET + RACKET_WIDTH and ball.dirc == LEFT) or (racket.side == RIGHT and ball.xcor() >= SCREEN_WIDTH - UPPER_RACKET - 10 and ball.dirc == RIGHT)):
				return True
		return False

	ball = Ball(3, 3, RIGHT)

	player_1= Racket('red', 0, LEFT, BOTTOM_RACKET, 5)
	player_2= Racket('blue', 1, RIGHT, BOTTOM_RACKET + 20, 5)
	player_3= Racket('yellow', 2, LEFT, UPPER_RACKET, 5)
	player_4= Racket('green', 3, RIGHT, UPPER_RACKET + 20, 5)

	RACKETS = [player_1, player_2, player_3, player_4]

	turtle.onkeypress(player_1.changeDir, 'q')
	turtle.onkeypress(player_2.changeDir, 'c')
	turtle.onkeypress(player_3.changeDir, 'm')
	turtle.onkeypress(player_4.changeDir, 'p')

	turtle.listen()

	while RUNNING:
		ball.move()
		for i in RACKETS:
			i.move()
		for i in POINTS:
			if i == 100:
				RUNNING = False
		turtle.update()
		time.sleep(SLEEP)