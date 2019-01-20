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

#definding the edges of the screen
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_width()/2


my_ball = Ball(100,100,20,20,50,"pink")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

#creating a list of balls
BALLS=[]

#iterating through all the balls in the list BALLS
for i in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	dx = random.randint( MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dy = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())

new_ball = Ball(x, dx, y, dy, r, color)
BALLS.append(new_ball)

#move all balls:
for ball in BALLS:
	ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)

#cheks for ball colilisions
def colide(ball_a, ball_b):
	if ball_a == ball_b:
		return False
	#distance between the 2 balls
	D = math.sqrt(math.pow((ball2.xcor()-ball1.xcor()),2) + math.pow((ball2.ycor()-ball1.ycor()),2))
	
	if  D+10 <= ball1.r + ball.r:
		return True 
	else:
		return False

#cheks collisions betwen any 2 balls
def all_balls_collision():
	for ball1 in BALLS:
		for ball2 in BALLS:
			if colide(ball1, ball2):
				#initialize new variables for the attributes of the new Ball
				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

				#makes sure dx or dy isnt = 0 
				dx = 0
				while dx == 0:
					dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				dy = 0
				while dy ==  0:
					dy = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)

				r = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				color = (random.random(), random.random(), random.random())
				new_ball = Ball(x, dx, y, dy, r, color)

				ball1.r = r1
				ball2.r = r2

				#Determine which ball is smaller\bigger + accordingly generate values to ball atributes
				if r1>r2 :
					r1 += 10
					ball1.r = r1
					ball1.shapesize(r1/10)
					ball2.goto(x,y)
					ball2.dx = dx
					ball2.dy = dy
					ball2.r = r
					ball2.shapesize(r/10)
					ball2.color(color)

				#Determine which ball is smaller\bigger + accordingly generate values to ball atributes
				if r2>r1 :
					r2 += 10
					ball2.r = r2
					ball2.shapesize(r2/10)
					ball1.goto(x,y)
					ball1.dx =dx
					ball1.dy = dy
					ball1.r = r
					ball1.shapesize(r/10)
					ball1.color(color)

#detect whether a collision happened between my_ball and another ball:
def myball_collision():
	for ball in BALLS:
		if colide(my_ball,ball):
			my_ball.r = my_r
			ball.r = ball_r






















		




