#Learning to print patterns 

#Square patterns  
n = int(input("enter a num")) 
for j in range (1, n+1): #outer loop which will iterate the code for every line
    for i in range(1, n+1):#inner loop which will print the n in the same line 
        if i != n:
            print(i, end=' ')
        else:
            print(i)

#Same question with pattern
n = int(input("Enter the size of the square: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


n2 = int(input("enter your number:"))

#Lets do this with alphabets

size = int(input("enter the size of the square: "))

for i in range(size):
    for j in range(size):
        print(chr(65+j), end="")
    print()