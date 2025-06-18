#Here you will not see any code cause i just run my code here for testing



size = int(input("enter the size of the pyramid: "))
n=65
for i in range(size):
    for j in range(size-i-1):
        print(" ", end=' ')
    for k in range(2*i+1):
        print(chr(n), end=' ')
   
    for l in range(size+i+1):
        print(" ", end=' ')
    for m in range(2*i-1):
        print(chr(n), end=' ')
    n+=1
    print()


