'''
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
		self.color(colors[c])




s = Square(8)
s.random_color()


turtle.mainloop()
'''
#Exercise 2
 
from turtle import Turtle 
import turtle 


class Hexagon(Turtle):
 	def __init__(self, size, hcolor):
 		Turtle.__init__(self)
 		self.size = size
 		self.hcolor = hcolor
 		turtle.penup()
 
 		turtle.begin_poly()
 		for i in range(6):
 			turtle.forward(100)
 			turtle.right(60)
 		turtle.end_poly()

 		s = turtle.get_poly()
 		turtle.register_shape("Hexagon", s)
 		self.shape("Hexagon")
 		self.shapesize(self.size)
 		self.color(self.hcolor)
h1 = Hexagon(2 ,"pink")

turtle.mainloop()