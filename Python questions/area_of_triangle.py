# Area of triangle
import math
def aot(a,b,c,p):
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
p = (a+b+c)/2
print("area of triangle is: ",aot(a, b, c, p) )