num1 = int(input("enter an integer: "))
num2 = int(input("enter an integer: "))
num3 = int(input("enter an integer: "))
num_list = []
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
for i in range (0,3):
    for j in range (0,3):
        for k in range (0, 3):
            if (i!=j and j!=k and k!=i):
                print(num_list[i], num_list[j], num_list[k])