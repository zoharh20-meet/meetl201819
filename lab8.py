from turtle import *
import random
import math
colliding = False


class Ball(Turtle):
	def __init__(self, radius, color, x, y, dx, dy):
		Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.x = x
		self.y = y
		self.goto(self.x, self.y)
		self.showturtle()
		self.dx = dx
		self.dy = dy
	def move(self,height,width):
		newx = self.xcor()+self.dx
		newy = self.ycor()+self.dy
		self.goto(newx,newy)
		if newx > width or newx <-width:
			self.dx = -self.dx

		if newy > height or newy <-height:
			self.dy = -self.dy

def check_collision(ball1, ball2):

	x1 = ball1.xcor()
	y1 = ball1.ycor()
	x2 = ball2.xcor()
	y2 = ball2.ycor()
	colliding = False
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	

	if D<= ball1.radius+ball2.radius:
		colliding = True
	return (colliding)




ball1 = Ball(20, "yellow",  100, 100,20,20)
ball2 = Ball(40, "pink", 0 ,0,10,10)

while True:
	ball1.move(200,200)
	ball2.move(200,200)

	


	c=check_collision(ball1, ball2)
	print(c)

turtle.mainloop()

