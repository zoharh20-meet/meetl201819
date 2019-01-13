import turtle 
from turtle import *
import time
import random
from ball import Ball
turtle.tracer(1)
turtle.hideturtle()

global RUNNING, SLEEP, SCREEN_WIDTH, SCREEN_HEIGHT

 RUNNING = True 
 SLEEP = 0.0077
 SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
 SCREEN_HEIGHT = turtle.getcanvas().winfo_width()/2

 my_ball = Ball(100,100,20,20,50,"pink")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX t = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

balls[]

for i in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	dx random.randint( MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dy = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())

new_ball = Ball(x, dx, y, dy, r, color)
balls.append(new_ball)

#move all balls:
for ball in balls:
	ball.move(screen_width,screen_height)

def colide(ball_a, ball_b):
	if ball_a == ball_b:
		




