#Here you will not see any code cause i just run my code here for testing


size = int(input("enter the number"))

for i in range(1, size+1):
    for j in range(size - i + 1):
        print(i, end='')
    print()