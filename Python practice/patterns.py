#Learning to print patterns 

#Square patterns  
n = int(input("enter a num")) 
for j in range (1, n+1): #outer loop which will iterate the code for every line
    for i in range(1, n+1):#inner loop which will print the n in the same line 
        if i != n:
            print(i, end=' ')
        else:
            print(i)

#Same question with star pattern
n = int(input("Enter the size of the square: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()




#Lets do this with alphabets

size = int(input("enter the size of the square: "))

for i in range(size):
    for j in range(size):
        print(chr(65+j), end="")
    print()

#Continue Number pattern

size = int(input())
n = 1

for i in range(size):
    for j in range (size):
        print(n, end=" ")
        n+=1
    print()

#Continue alphabet pattern

size = int(input("enter the size of the pattern"))

n = 65

for i in range(size):
    for j in range(size):
        print(chr(n), end='')
        n+=1
    print()

#Single side triangle pattern

size = int(input("enter the size of the star: "))
for i in range(size):
    for j in range(i+1):
        print("*", end='')
        i+1
    print()

#Same question with numbers

size = int(input("enter the size: "))
for i in range(1, size+1):
    for j in range(i):
        print(i, end='')
    print()

#Floyds triangle pattern 
size = int(input("enter the size of the triangle:"))

n = 1

for i in range(1, size+1):
    for j in range(i):
        print(n, end='')
        n+=1
    print()