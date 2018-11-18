##import tkinter as tk
#from tkinter import simpledialog
#Then when ever you want to ask the user for input use this code
#greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
#if greeting != ("Arrr!") :
#	print("Go away, pirate")
#else:
	#print("Greetings, hater of pirates!")



#problem 2
# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

#import tkinter as tk
#from tkinter import simpledialog

#year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw()))

#if year <= 1900:
 #   print ("Woah, that's the past!")
#elif year > 1900 and year < 2020:
 #   print ("That's totally the present!")
#else:
 #   print ("Far out, that's the future!!")


#Problem 3

# Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".

#class Person(object):
'''
  def __int__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def speak(self):
  	print("My name is " + self.first_name + " " + self.last_name)
  	'''

#me = Person("Brandon", "Walsh")
#you = Person("Ethan", "Reed")

#me.speak()
#you.speak()






#Problem Four:
import tkinter as tk
from tkinter import simpledialog
# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.
'''
exam_one = int(simpledialog.askstring("Input", "Input exam grade one: ", parent=tk.Tk().withdraw()))

exam_two = int(simpledialog.askstring("Input"," exam grade two: " , parent=tk.Tk().withdraw()))

exam_3 = int(simpledialog.askstring("Input", "exam grade three: ", parent=tk.Tk().withdraw()))

grades = [exam_one, exam_two, exam_3]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
   	 letter_grade = "D"
elif avg <= 64: 
	letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade is "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")

'''
#problem 5
'''

class Person():
   def __init__(self, name, favorite_food, Chocolate ,age, color):
       self.name = name
       self.fav_food = favorite_food
       self.age = age
       self.color = color



   def define_color(self, color):
       self.color = color

   def print_info(self):
       print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
       print("My favorite food is " + self.fav_food + " and my favorite color is " + self.color)


a = Person("Britney", "Pizza", "white", 16, "blue")
a.define_color("Black")
a.print_info()

b = Person("Jake", "omlet" , "dark" , 15 ,"orange")
b.print_info()

'''
#problem 6
'''
class Bear(object):
	def __init__(self, name):
		self.name = name
	def create(self):	
		print("A new bear created. Its name is: " + self.name)
	
	def say_hi(self):
		print("Hi! I’m a bear. My name is " + self.name)
my_bear = Bear("Danny")
print(my_bear.say_hi())

'''
#problem 7
'''
class Story(object):
	def __init__(self, n_balloons, name, color):
		self.n_balloons = n_balloons
		self.name = name
		self.color = color

	def tell(self):
		print("This is a tale about " + self.n_balloons + " balloons. The first kid is " + self.name + " who got a " + self.color + "balloon" )

my_story = Story("5", "Ron", "Yellow")
print(my_story.tell())
'''
#Problem 8
'''

class Cake(object):
	def __init__(self, flavor):
		self.flavor = flavor

	def eat(self):
		print("Yummy!!! Eating a " + self.flavor + " cake" )

cake = Cake("chocolate")
print(cake.eat())
# what I want to be printed: Yummy!!! Eating a chocolate cake :)

'''
#Problem 9
'''

class Cat(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def birthday(self):
		self.age += 1
		if self.age >= 100:
			print("Dong dong, the cat is dead!")
		else:
			print(self.name + "hasing its " + str(self.age) +" birthday!")

my_cat = Cat("Salem", 7)
print (my_cat.birthday())
# what I want: my cat to celebrate its 8th birthday (and all the 
# birthdays that come before that)


'''	