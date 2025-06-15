#Here you will not see any code cause i just run my code here for testing


size = int(input("enter the size of the triangle"))
n = 1
for i in range (1, size+1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()