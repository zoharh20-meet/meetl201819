from turtle import Turtle
import turtle
import random
class Square(Turtle):
	def __init__(self, size ):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")
		

	def random_color (self):
		colors = ["yellow", "pink", "blue", "green"]
		c= random.randint(0,3)
		self.color(color[c])




s = Square(8)
s.random_color()


turtle.mainloop()