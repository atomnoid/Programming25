# size = int(input("enter the size of the star: "))
# n = 65
# for i in range(1, size+1):
#     for j in range(i+1):
#         print(chr(n+1), end='')
#         i+=1
#      print()

#Floyds triangle patterm
size = int(input("enter the size of the triangle:"))

n = 1

for i in range(1, size+1):
    for j in range(i):
        print(n, end='')
        n+=1
    print()
 
 