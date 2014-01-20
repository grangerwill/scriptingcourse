"""
Week 1: Example 3: Dictionary Manipulation

Disctionaries are associative collections of objects. 

Python allows you to collect any object in a disctionary, 
but it does place restrictions on keys (they must be string or number)
"""

__author__ =  'Bernie Hogan'
__version__=  '1.0'

LB = "\n-----------------------"

print "Lists work in sequence, and are indexed by a number"
print "Dictionaries are indexed by keys. They are extremely useful."
print "A list is enclosed in [], a dictionary in {}."

# a and Cheez is a KEY VALUE PAIR - here there are FOUR key value pairs
# A key value in a dict is ALWAYS A STRING. The differing use of '' and "" below is arbtitrary
dict1 = {'a':"Cheez",'b':"Ham",'c':"Veggie",'d':"Fish"}
print dict1

print LB
print "Dictionaries are iterable through 'items', 'values' or 'keys'"

print dict1.keys()

for i in dict1.keys(): 
	print i

print

for i in dict1.values(): 
	print i

# BIG FINAL STEP
print

for i,j in dict1.items(): 
	print i + ":" + j

print LB
print "You can reference a dictionary's value by its key,"
print "but not the other way around."

if dict1.has_key("d"):
	print "I don't really like " + dict1["d"] + "burgers."


dict1["e"] = "chicken"

if dict1.has_key("chicken"):
	print "I think " + dict1["Ham"] + "burgers are okay"
else:
	print "Someone looking for a Hamburger?"

# use the 'if' function in case your dict does not have a particular key 
if dict1.has_key('a'):
	print "I luv " + dict1["a"] + "burgers."
	
