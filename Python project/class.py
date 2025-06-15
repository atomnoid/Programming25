size = int(input("enter the size: "))

n = 65

for i in range(size):
    for j in range(i+1):
        print(chr(n+i), end='')
    print()
