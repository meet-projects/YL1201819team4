import turtle
import random
import time
from turtle import Turtle, Screen
turtle.addshape('uri.gif')
turtle.addshape('snake.gif')
additions=[0,0,0,0]
def play_reaction():
	global player
	global additions
	global good, bad
	global RUNNING
	global win
	global players

	headline1 = turtle.clone()
	turtle.hideturtle()
	headline1.hideturtle()
	headline1.penup()
	headline1.goto(0,350)
	headline1.color("black")
	headline1.write("REACTION - press ONLY when there is a panda!", align = "center", font=("Comic Sans MS", 50, "bold"))



	class player(Turtle):
		def __init__(self, color, x, y, condition, index):
			Turtle.__init__(self)
			self.penup()
			self.color(color)
			self.shape('square')
			self.speed(0)
			self.goto(x, y)
			self.index=index
			self.shapesize(1)
			self.condition= condition
		
		def press(self):
			global RUNNING
			for i in players:	
				if(i.condition == 2):
					return 0
			if win==1 and self.condition !=1: 
				self.shapesize(2)
				self.sety(-110)
				self.condition = 2
				additions[self.index]+=25
				RUNNING=False
			else:
				self.color('black')
				self.condition = 1


	good = turtle.Turtle()
	bad = turtle.Turtle()
	TURTLES = [good, bad]

	for i in TURTLES:
		i.hideturtle()
		i.goto(0,0)
		i.left(90)
		turtle.shape("triangle")
		i.shapesize(10)
		if i == bad:
			i.shape("snake.gif")
		else:
			i.shape('uri.gif')

	RUNNING = True
	
	player_1= player('red', -150, -125, 0, 0)
	player_2= player('blue', -50, -125, 0, 1)
	player_3= player('yellow', 50, -125, 0, 2)
	player_4= player('green', 150, -125, 0, 3)
	players = [player_1, player_2, player_3, player_4]

	turtle.onkeypress(player_1.press, 'q')
	turtle.onkeypress(player_2.press, 'c')
	turtle.onkeypress(player_3.press, 'm')
	turtle.onkeypress(player_4.press, 'p')
	turtle.listen()
	win = 0
	start = time.time() + random.randint(3, 5)
	while RUNNING:
		turtle.update()
		if time.time() > start:
			RUNNING = False
	#time.sleep(random.randint(5, 8))
	
	while random.randint(0, 1):
		RUNNING = True
		win = 0
		bad.showturtle()
		start = time.time() + 4
		while RUNNING:
			turtle.update()
			if time.time() > start:
				RUNNING = False
		bad.hideturtle()
		RUNNING = True
		start = random.randint(3, 5) + time.time()
		while RUNNING:
			turtle.update()
			if time.time() > start:
				RUNNING = False

	win = 0
	win = 1
	bad.hideturtle()
	good.showturtle()
	#wait random time
	
	RUNNING = True

	start = time.time() + 4

	while RUNNING:
			turtle.update()
			if time.time() > start:
				RUNNING = False

# pygame.event.pump()
#     keys = pygame.key.get_pressed()
  
#     if keys[pygame.K_p]:
#         player_1.score=i+1
# 		player_1.score=i

#     if keys[pygame.K_c]:
#         player_2.score=i+1
# 		player_2.score=i

#     if keys[pygame.K_n]:
#         player_3.score=i+1
# 		player_3.score=i

#     if keys[pygame.K_p]:
#         player_4.score=i+1
# 		player_4.score=i
