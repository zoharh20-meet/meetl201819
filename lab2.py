list1= [1,3,4,5]
list2 = [2,4,6]
list3 = []
def lists ():
	for number in list1:
		for i in list2:
			if i == number: 
				list3.append(number)
		print(list3)
lists()

a= [1,2,3,4,5,10,20,21,34,55]
for number in  a:
 	if number<5:
	    print (number)


c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def common():
 for index in c:
  for index2 in b:
  	if index2 == index:
  	 print (index)

common ()

 


