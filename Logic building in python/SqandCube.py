# In this program i will use very basics of functions to find square and cube of a numnber

def square (num): # defining a function to find square of a number
   return num*num
def cube (num):
   return num*num*num # defining a function to find cube of a number
number = int(input("enter your number: "))
print("The square of the number is: ", square(number))
print("The cube of the number is: ", cube(number))