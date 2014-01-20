"""Multiple
Lines"""

__author__ = 'WG'
__version__ = '1.0'

print "hello \"world\""

#two types of variable: str (string) and int (integer) - these are reserved functions.
x = 4
y = "square"
z = 1
print str(int(x) + z) + y

# In general, variables in CAPS are constants / vars starting with Caps are 'objects' (generic term - can be a string object, a list object, etc.)
    # / variables with nocaps are variables
# Naming vars:
#Option 1:
old_list = ["hello", "good sir"]
#Option 2:
oldList = ["what ho", "motherfucker","?"]

# Append variable type:
userNames = ["x","y"]
userNamesList = ["z","a"]
lUserNames = ["r","w"]

# Dictionary of user userNames:
dUserNames = {"Bernie":"Man","Julia":"Woman"}

# Python doesn't require you to tell it which variable is what sort - so use lists [], dictionaries {} and tuples ()

# ctrl + / = add # to the start of a line

# See what you can do to a method: Start>CMD>python then dir("x") or dir(5) - i.e. what can I do with this object, what methods - and also another way for i in dir("x"): print i
# Help tells us the details of each method available to the object that dir threw up: help("x".upper) OR help("x".count) etc.