import time
import turtle
from turtle import Turtle
from scoreboard import show_scoreboard
import race
from race import play_race
import reaction
from reaction import play_reaction
import pong
from pong import play_pong


GAMES = ["race", "reaction", "pong"]
ROUNDS = 3
POINTS = [0,0,0,0]

def game(game):
	AMOUNT_REACTION = 3
	if game == "race":
		play_race()
		for i in range(len(POINTS)):
			POINTS[i] += race.additions[i]
		race.additions = [0, 0, 0, 0]
	elif game == "reaction":
		for i in range(AMOUNT_REACTION):
			play_reaction()
			turtle.clearscreen()
		for i in range(len(POINTS)):
			POINTS[i] += reaction.additions[i]
		reaction.additions = [0, 0, 0, 0]

	elif game == "pong":
		play_pong()
		for i in range(2):
			POINTS[i] += pong.POINTS[i]
			POINTS[i + 2] += pong.POINTS[i]
		pong.POINTS = [0, 0]
		
for i in GAMES:
	turtle.clearscreen()
	show_scoreboard(POINTS[0], POINTS[1], POINTS[2], POINTS[3], False)
	turtle.clearscreen()
	game(i)		
	turtle.clearscreen()

show_scoreboard(POINTS[0], POINTS[1], POINTS[2], POINTS[3], True)




turtle.mainloop()