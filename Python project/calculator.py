# In this program i am making a very simple calculator using python

def switch():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print ("For addition press 1\n For substraction press 2\n For multiplication press 3\n For division press 4\n For modulus press 5\n For power press 6\n")
    option = int(input("Enter the option: "))
    if option == 1:
        print ("The addition is: ", a+b)
    elif option == 2:
        print ("The substraction is: ", a-b)
    elif option == 3:
        print ("The multiplication is: ", a*b)
    elif option == 4:
        print ("The division is: ", a/b)
    elif option == 5:
        print ("The modulus is: ", a%b)
    elif option == 6:
        print ("The power is: ", a**b)
    else:
        print("Invalid option")
switch()