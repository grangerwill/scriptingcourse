"""
Week 1: Debugging exercise 2. Debugging List Operations 

Each one of these exercises requires you to alter the code in some way. 
If the code works properly then it will run up until that point and then stop.

Each exercise should require only one kind of change/alteration.
"""

__author__ =  'Bernie Hogan'
__version__=  '1.0'

#1. Create a list - NONE is an empty variable
list1 = ["1","2","3","4",None,"5"]

#2. Create a second list
list2 = ["6","7","8","9","10"]

#3. Concatenate two lists - MAKE SURE THE BRACKETS ARUND LIST 1 AND 2 ARE THE SAME - [] FOR A LIST
list3 = list1 + list2

#4. Iterate through a list
for i in list3:
	print i
	
#5. Iterate through a list by assignment - the lists should match  (WAS: print list1[i], but list 1 too short)
for i in range(len(list3)):
	print list3[i]
	
# 6. Replace one list element with another
list1[0] = list2[1]

#7. Adding one element to a list
list1 = list1 + ["new element"]
# OR list1 = list1.append("new element")

#8. Operating on a list: (list comprehension: allows us to do something to each item in the list and gen a new list)
#Here we're t
oldList = [1,4,3,2,6]
newList = [x for x in oldList if str(x)]
# OR newList = [str(x) for x in oldList]

print "Finally! I thought it would take forever."