#class Animal(object):
#	def __init__(self,sound,name,age,favorite_color,):
#		self.sound = sound
#		self.name = name 
#		self.age = age
#		self.favorite_color = favorite_color
		
	
#	def eat(self,food):
#		print("Yummy!" + self.name + " is eating " + food)
	
#	def descripsion(self):
#			print(self.name + "is " +self.age + " years old and loves the color " +self.favorite_color)
#
#	def make_sound(self):
#		print(self.sound*3)

#z = Animal("meow", "zebra ", " 15", "crimson", )
#z.eat("people")
#z.descripsion()
#z.make_sound()


class Person(object):
	def __init__(self, name, age, city, gender):
		self.name = name
		self.age = age
		self.gender =  gender


c = Person("clara", "18", "Jerusalem", "girl")

	def eat(self,food):
		print(self.name + " eats " + food)

c.eat("Hamin")