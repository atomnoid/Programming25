#Here you will not see any code cause i just run my code here for testing


size = int(input("enter your size:"))

for i in range (1, size+1):
    for j in range(i - 1):
        print(" ", end=' ')
    for k in range(size - i + 1):
        print(i, end=' ')
    print()

size = int(input("Enter the number of rows: "))

for i in range(1, size + 1):
    for j in range(i - 1):
        print(" ", end=" ")
    for k in range(size - i + 1):
        print(i, end=" ")
    print()
