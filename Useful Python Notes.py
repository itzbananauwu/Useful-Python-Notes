#Author: Terry Su 
#Purpose: some useful notes and tips

#THE ALL() & ANY() FUNCTION

#The all() function returns True if all items in an iterable are true, otherwise it returns False.
#If the iterable object is empty, the all() function also returns True.

#Params:
#the iterable

#Note: When used on a dictionary, the all() function checks if all the keys are true, not the values.

#Examples:
x = [1,2,0]
print(all(x))
b#You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

#Syntax:
#sorted(iterable, key=key, reverse=reverse)

#Params:
#iterable - The sequence to sort, list, dictionary, tuple etc.
#key (Optional) - A Function to execute to decide the order. Default is None
#reverse(Optional) - A Boolean. False will sort ascending, True will sort descending. Default is False

#sorted(iterable, key=key, reverse=reverse)

#Examples:
l = ['a','g','b']
print(sorted(l))
x = [1,3,5,2,5]
print(sorted(x), '\n')





#THE MAP() FUNCTION

#The map() function executes a specified function for each item in an iterable.
#The item is sent to the function as a parameter.

#Syntax:
#map(function, iterables)

#Params:
#function - The function to execute for each item
#iterables - A sequence, collection or an iterator object.
#            You can send as many iterables as you like, just make sure the function has one parameter for each iterable.

#Examples:
def length(element):
    return len(element)

output = list(map(length, ['dd','ggg','dffgg'])) #convert to list for readability
print(output)

output = list(map(lambda x,y: x + y, [1,2,3,4],[2,3,4,5]))
print(output, '\n')

#The Try Except structure:

#The "try" block lets you test a block of code for errors before excuting it.
#The "except" block lets you handle the error.
#The "finally" block lets you execute code, regardless of the result of the try- and except blocks.

#You can define as many exception blocks as you want,
#e.g. if you want to execute a special block of code for a special kind of error:

#The "finally" block, if specified, will be executed regardless if the try block raises an error or not.

#Examples:
try:
  print(var)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print(var)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished", '\n')





#Concept: variable "deep copy" vs "shallow copy"

#Shallow Copy	
#stores the references of objects to the original memory address.   	
#reflects changes made to the new/copied object in the original object.
#stores the copy of the original object and points the references to the objects.	
#Shallow copy is faster.

#Ex: copying an instance in a class or a nested array in a matrix (default)

#Deep Copy
#stores copies of the object’s value.
#doesn’t reflect changes made to the new/copied object in the original object.
#stores the copy of the original object and recursively copies the objects as well.
#Deep copy is comparatively slower.

#Ex: a function passing a variable or copying a simple variable x = 3 (default)

# implementation of the Deep
from copy import copy, deepcopy
 
# Class of Car
class Car:
  def __init__(self, name, colors):
     
     self.name = name
     self.colors = colors
     
honda = Car("Honda", ["Red", "Blue"])
 
# Deepcopy of Honda
deepcopy_honda = deepcopy(honda)
deepcopy_honda.colors.append("Green")
print(deepcopy_honda.colors, \
      honda.colors)
 
# Shallow Copy of Honda
copy_honda = copy(honda)
 
copy_honda.colors.append("Green")
print(copy_honda.colors, \
      honda.colors, '\n')

# Break/Continue Keyword
condition = True
numbers = [1,2,3,4]
for a in numbers:
    if condition:
        break # Stops looping the code
    else:
        continue # Continue looping



#Data structure: sets

#Sets are used to store multiple items in a single variable. (mostly used for fast lookup)
#Set is one of 4 built-in data types in Python used to store collections of data and similar to values in a hash table
#A set is a collection which is both UNORDERED and UNINDEXED.
#A set CANNOT contain DUPLICATES either
#Sets are written with curly brackets.

#Ex:
s = {1,2,3,4}




#Bitwise Operations: https://wiki.python.org/moin/BitwiseOperators
